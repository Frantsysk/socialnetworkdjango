from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Profile, Message, Post, Comment


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
        fields = ['age', 'country', 'gender', 'bio', 'picture', 'cover_picture','facebook_url', 'instagram_url', 'google_url', 'email', 'work_place']
        # exclude = ['owner']
        model = Profile
        widgets = {
            'age': forms.NumberInput(attrs={'placeholder': 'age', 'class': 'single-field'}),
            'country': forms.TextInput(attrs={'placeholder': 'country', 'class': 'single-field'}),
            'gender': forms.TextInput(attrs={'placeholder': 'your gender', 'class': 'single-field'}),
            'bio': forms.Textarea(attrs={'placeholder': 'tell the world about yourself', 'class': 'single-field', 'rows': 5}),
            'picture': forms.ClearableFileInput(attrs={'class': 'single-field'}),
            'cover_picture': forms.ClearableFileInput(attrs={'class': 'single-field'}),
            'facebook_url': forms.TextInput(attrs={'placeholder': 'facebook url', 'class': 'single-field'}),
            'instagram_url': forms.TextInput(attrs={'placeholder': 'instagram url', 'class': 'single-field'}),
            'google_url': forms.TextInput(attrs={'placeholder': 'google link', 'class': 'single-field'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email', 'class': 'single-field'}),
            'work_place': forms.TextInput(attrs={'placeholder': 'work place', 'class': 'single-field'})
        }


class MessageForm(ModelForm):
    class Meta:
        fields = ('text', 'image')
        model = Message
        widgets = {
        'text': forms.Textarea(attrs={'placeholder': 'Text', 'class': 'single-field'})
        }


class PostForm(ModelForm):
    class Meta:
        fields = ('title','text', 'image')
        model = Post
        widgets = {
        'text': forms.Textarea(attrs={'placeholder': 'Text', 'class': 'single-field'})
        }

class CommentForm(ModelForm):
    class Meta:
        fields = ('content', 'image')
        model = Comment



    # country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country', 'class': 'single-field'}))
    # bio = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Bio', 'class': 'single-field'}))
    # picture = forms.ImageField(widget=forms.ImageField(attrs={'class': 'single-field'}))
    # gender = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Gender', 'class': 'single-field'}))
    # age = forms.IntegerField(widget=forms.IntegerField(attrs={'placeholder': 'Age', 'class': 'single-field'}))