from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/signin.html', {'form': form})
