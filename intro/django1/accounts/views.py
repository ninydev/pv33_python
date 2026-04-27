
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Декоратор проверяет сессию: если гость — кидает на страницу логина, если свой — пускает дальше.
@login_required
def profile(request):
    # request.user — это объект текущего авторизованного пользователя
    return render(request, 'accounts/profile.html')