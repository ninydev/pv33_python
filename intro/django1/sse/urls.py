from django.urls import path
from . import views

urlpatterns = [
    path('stream/', views.stream_view, name='sse_stream'),
    path('test/', views.sse_test_page, name='sse_test'),
    path('send/', views.send_test_message, name='sse_send'),
]
