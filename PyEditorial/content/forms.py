from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser
# Custom SignUp Form - Optional, if you want to add custom fields
class CustomSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # Not 'User'
        fields = ('username', 'email', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

# Search form (as requested in your original form structure)
class SearchForm(forms.Form):
    query = forms.CharField()
