from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustomAuthForm
from .forms import RegistrationForm
from django.contrib.auth import login, logout


def index(request):
    return render(request, 'index.html')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

    form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect('/')