from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms


class CustomAuthForm(AuthenticationForm):
    def clean(self):
        email = self.cleaned_data.get("email")

        if email:
            self.user_cache = authenticate(
                self.request,
                username=email,
                password=self.cleaned_data.get("password")
            )

            if self.user_cache is None:
                raise forms.ValidationError(
                    "Invalid email or password"
                )
        return self.cleaned_data


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]