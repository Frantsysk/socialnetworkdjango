from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            auth = authenticate(request, username=username, password=password)
            login(request, auth)
            Profile.objects.create(owner = request.user)
            return redirect('profile')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    context = {'form': CustomUserCreationForm()}
    return render(request, 'NetworkApp/signup.html', context)


def edit_profile(request):
    profile = Profile.objects.get(owner = request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    context = {'form': ProfileForm(instance=profile)}
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





