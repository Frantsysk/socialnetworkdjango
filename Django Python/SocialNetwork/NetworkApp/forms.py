from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        model = get_user_model()
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'single-field'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'single-field'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'single-field'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'single-field'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'single-field'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'single-field'}))


class ProfileForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Profile

    # country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country', 'class': 'single-field'}))
    # bio = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Bio', 'class': 'single-field'}))
    # picture = forms.ImageField(widget=forms.ImageField(attrs={'class': 'single-field'}))
    # gender = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Gender', 'class': 'single-field'}))
    # age = forms.IntegerField(widget=forms.IntegerField(attrs={'placeholder': 'Age', 'class': 'single-field'}))

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'single-field'


