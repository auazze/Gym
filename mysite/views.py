from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserForm, ClientForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    try:
        return render(request, 'mysite/home.html')
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        client_form = ClientForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserForm()
        client_form = ClientForm()
    return render(request, 'mysite/register.html', {'user_form': user_form, 'client_form': client_form})
