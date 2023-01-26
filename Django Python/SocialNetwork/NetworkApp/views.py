from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import authenticate, login


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    context = {'form': CustomUserCreationForm()}
    return render(request, 'NetworkApp/signup.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    context = {'form': ProfileForm()}
    return render(request, 'NetworkApp/edit_profile.html', context)


def profile_view(request):
    return render(request, 'NetworkApp/profile.html')


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('profile')
        else:
            messages.error(request, 'invalid input')
            return redirect('signup')





