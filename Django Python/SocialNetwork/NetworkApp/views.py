from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile, Friend
from django.contrib.auth.models import User


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
    context = {'form': ProfileForm(instance=profile), 'profile': profile}
    return render(request, 'NetworkApp/edit_profile.html', context)


def profile_view(request):
    return render(request, 'NetworkApp/profile.html')

def about_view(request):
    profile = Profile.objects.get(owner = request.user)
    my_friends = Friend.objects.filter(owner=request.user)
    friends_id = list(map(lambda friend: friend.friends.id, my_friends))
    show_friends = User.objects.filter(id__in = friends_id)
    display_users = User.objects.all().exclude(id__in = friends_id).exclude(id = request.user.id)
    context = {'profile': profile, 'users': display_users, 'friends': show_friends}
    return render(request, 'NetworkApp/about.html', context)


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

def add_friend(request, pk):
    owner = request.user
    friend = User.objects.get(id=pk)
    Friend(owner=owner, friends=friend).save()
    return redirect('about')

def add_friend(request, pk):
    owner = request.user
    friend = User.objects.get(id=pk)
    Friend(owner=owner, friends=friend).save()
    return redirect('about')

def delete_friend(request, pk):
    owner = request.user
    friend = User.objects.get(id=pk)
    Friend.objects.filter(owner=owner, friends=friend).delete()
    return redirect('about')







