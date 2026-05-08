from feedback.models import Feedback
from django import forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['firstName', 'lastName', 'email', 'phone', 'message']