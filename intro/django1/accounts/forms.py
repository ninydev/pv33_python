from django import forms
from .models import CustomUser

class UserAvatarForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']
