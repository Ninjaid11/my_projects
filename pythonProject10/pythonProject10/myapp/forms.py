from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Product
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'