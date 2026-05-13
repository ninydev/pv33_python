// Простой клиент для работы с Server-Sent Events (SSE)

function initSSE(streamUrl, onMessageCallback) {
    console.log("Connecting to SSE stream:", streamUrl);
    const eventSource = new EventSource(streamUrl);

    // Обработка входящих сообщений
    eventSource.onmessage = function(event) {
        try {
            const data = JSON.parse(event.data);
            console.log("Received SSE data:", data);
            if (onMessageCallback) {
                onMessageCallback(data);
            }
        } catch (e) {
            console.error("Error parsing SSE data:", e, event.data);
        }
    };

    // Обработка ошибок
    eventSource.onerror = function(error) {
        console.error("SSE connection error. Browser will try to reconnect automatically.", error);
    };

    // Возвращаем объект для возможности ручного закрытия
    return eventSource;
}

// Экспортируем функцию глобально, если нужно
window.initSSE = initSSE;
