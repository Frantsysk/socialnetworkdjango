from django.urls import path
from .views import signup_view, profile_view, edit_profile, login_action
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup', signup_view, name='signup'),
    path('profile', profile_view, name='profile'),
    path('login', login_action, name='login'),
    path('edit_profile', edit_profile, name='edit_profile')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


