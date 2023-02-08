from django.urls import path
from .views import signup_view, profile_view, edit_profile, login_action, about_view, add_friend, delete_friend
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup', signup_view, name='signup'),
    path('profile', profile_view, name='profile'),
    path('login', login_action, name='login'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('about', about_view, name='about'),
    path('add_friend/<int:pk>', add_friend, name='add_friend'),
    path('detele_friend/<int:pk>', delete_friend, name='delete_friend')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


