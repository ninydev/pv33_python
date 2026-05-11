from django.shortcuts import render
from django.views.decorators.http import require_POST

from feedback.forms import FeedbackForm
from feedback.models import Feedback

# Create your views here.
def show_feedback(request):
    cover_data = {
        'bg_image': '/static/images/hero_1.jpg',  # Или путь из статики/медиа, если нужно
        'title': 'Contact',
        'description': 'Send some text to me.'
    }

    action_message = ''
    if request.method == 'POST':
        feedback = Feedback()
        feedback.firstName = request.POST['firstName']
        feedback.lastName = request.POST['lastName']
        feedback.email = request.POST['email']
        feedback.phone = request.POST['phone']
        feedback.message = request.POST['message']
        if request.user.is_authenticated:
            feedback.user = request.user
        action_message = 'Feedback submitted successfully!'
        feedback.save()
    form = FeedbackForm()
    return render(request, 'pages/contact.html',
                  {'form': form, 'message' :action_message, "cover": cover_data})
