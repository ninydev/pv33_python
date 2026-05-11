from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from newsletters.models import NewsSubscriber

@require_POST
def subscribe(request):
    email = request.POST.get('email')
    if not email:
        return JsonResponse({'error': 'Email is required.'}, status=400)

    subscriber, created = NewsSubscriber.objects.get_or_create(email=email)

    if not subscriber.is_active:
        # send email
        return JsonResponse({'message': 'Thank you for subscribing!. Check email'})

    return JsonResponse({'message': 'You are already subscribed.'})




def unsubscribe(request):
    email = request.GET.get('email')
    token = request.GET.get('token')
    if not email or not token:
        return JsonResponse({'error': 'Email and token are required.'}, status=400)

    try:
        subscriber = NewsSubscriber.objects.get(email=email, token=token)
    except NewsSubscriber.DoesNotExist:
        return JsonResponse({'error': 'Invalid email or token.'}, status=400)

    subscriber.is_active = False
    subscriber.save()

    return JsonResponse({'message': 'You have been unsubscribed.'})


def confirm_subscription(request):
    email = request.GET.get('email')
    token = request.GET.get('token')
    if not email or not token:
        return JsonResponse({'error': 'Email and token are required.'}, status=400)

    try:
        subscriber = NewsSubscriber.objects.get(email=email, token=token)

        subscriber.is_active = True
        subscriber.save()
        return JsonResponse({'message': 'Your subscription has been confirmed.'})

    except NewsSubscriber.DoesNotExist:
        return JsonResponse({'error': 'Invalid email or token.'}, status=400)


