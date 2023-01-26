from django.urls import path
from .views import signup_view, profile_view, login_action, edit_profile

urlpatterns = [
    path('signup', signup_view, name='signup'),
    path('profile', profile_view, name='profile'),
    path('login', login_action, name='login'),
    path('edit_profile', edit_profile, name='edit_profile')
]


