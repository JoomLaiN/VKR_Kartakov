from django import forms
from users.models import User

from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    
    
    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password']