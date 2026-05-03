
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserAvatarForm

# Декоратор проверяет сессию: если гость — кидает на страницу логина, если свой — пускает дальше.
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserAvatarForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserAvatarForm(instance=request.user)
    
    # request.user — это объект текущего авторизованного пользователя
    return render(request, 'accounts/profile.html', {'form': form})