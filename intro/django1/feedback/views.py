from django.shortcuts import render
from django.views.decorators.http import require_POST

from feedback.forms import FeedbackForm
from feedback.models import Feedback

# Create your views here.
def show_feedback(request):
    if request.method == 'POST':
        feedback = Feedback()
        feedback.firstName = request.POST['firstName']
        feedback.lastName = request.POST['lastName']
        feedback.email = request.POST['email']
        feedback.phone = request.POST['phone']
        feedback.message = request.POST['message']
        if request.user.is_authenticated:
            feedback.user = request.user
        feedback.save()
    form = FeedbackForm()
    return render(request, 'pages/contact.html', {'form': form})
