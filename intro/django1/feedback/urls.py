from django.urls import path

from feedback.views import show_feedback

app_name = 'feedback'

urlpatterns = [
    path('', show_feedback, name='feedback'),
]