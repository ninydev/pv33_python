from django.http import HttpResponse

def hello_world(request):
    # request — это объект, содержащий все данные о запросе (заголовки, IP, параметры)
    return HttpResponse("<h1>Привет, PV33! Это наш первый ответ от Django.</h1>")