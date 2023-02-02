from django.urls import path
from .views import signup_view, profile_view, edit_profile, login_action, about_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup', signup_view, name='signup'),
    path('profile', profile_view, name='profile'),
    path('login', login_action, name='login'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('about', about_view, name='about')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


