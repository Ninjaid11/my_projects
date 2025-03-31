from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignupForm


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            return HttpResponse(f'Спасибо за регистрацию, {name}!')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})