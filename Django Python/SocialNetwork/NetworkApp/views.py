from django.shortcuts import render
from django.contrib import messages
from .forms import CustomUserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    context = {'form': CustomUserCreationForm()}
    return render(request, 'NetworkApp/signup.html', context)


def profile_view(request):
    return render(request, 'NetworkApp/profile.html')


