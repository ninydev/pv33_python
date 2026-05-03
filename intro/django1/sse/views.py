import json
import time
import queue
import threading
from datetime import datetime
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Глобальная коллекция соединений: {user_id: [Queue, ...]}
# Используем Lock для потокобезопасности при работе со словарем
user_connections = {}
connections_lock = threading.Lock()

def stream_view(request):
    """
    Контроллер для поддержания SSE соединения.
    """
    # Складываем пользователей в коллекции по user_id
    user_id = request.user.id if request.user.is_authenticated else "anonymous"
    q = queue.Queue()
    
    with connections_lock:
        if user_id not in user_connections:
            user_connections[user_id] = []
        user_connections[user_id].append(q)
    
    def event_stream():
        try:
            # Начальное приветствие в формате JSON
            yield f"data: {json.dumps({'status': 'connected', 'user_id': user_id})}\n\n"
            
            while True:
                try:
                    # Ждем данные из очереди (блокирующее чтение с таймаутом)
                    message = q.get(timeout=20)
                    yield f"data: {json.dumps(message)}\n\n"
                except queue.Empty:
                    # Heartbeat для поддержания соединения активным
                    yield ": heartbeat\n\n"
        except Exception:
            pass
        finally:
            # Удаляем очередь при разрыве соединения
            with connections_lock:
                if user_id in user_connections:
                    if q in user_connections[user_id]:
                        user_connections[user_id].remove(q)
                    if not user_connections[user_id]:
                        del user_connections[user_id]

    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    response['X-Accel-Buffering'] = 'no'
    return response

def broadcast_time():
    """
    Фоновый процесс: шлет всем время каждые 10 секунд.
    """
    while True:
        time.sleep(10)
        now = datetime.now().strftime("%H:%M:%S")
        msg = {'type': 'server_time', 'time': now}
        
        with connections_lock:
            # Копируем список ключей для безопасной итерации
            for uid in list(user_connections.keys()):
                for q in user_connections[uid]:
                    q.put(msg)

# Запуск фонового таймера
threading.Thread(target=broadcast_time, daemon=True).start()

def sse_test_page(request):
    """Страница для отображения работы SSE"""
    return render(request, 'sse/test_sse.html')

def send_test_message(request):
    """API для отправки сообщения текущему пользователю"""
    user_id = request.user.id if request.user.is_authenticated else "anonymous"
    msg_text = request.GET.get('msg', 'Тестовое сообщение')
    
    count = 0
    with connections_lock:
        if user_id in user_connections:
            for q in user_connections[user_id]:
                q.put({'type': 'direct_message', 'text': msg_text})
                count += 1
    
    return JsonResponse({'status': 'ok', 'sent_to_sessions': count})
