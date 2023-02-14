from django.urls import path
from .views import signup_view, profile_view, edit_profile, login_action, about_view, add_friend, delete_friend, user_about, message_view, message_delete, message_update, create_post, delete_post, post_update, create_comment, delete_comment, feed_view, like_view, dislike_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('login/', login_action, name='login'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('about/', about_view, name='about'),
    path('add_friend/<int:pk>/', add_friend, name='add_friend'),
    path('detele_friend/<int:pk>/', delete_friend, name='delete_friend'),
    path('user_about/<int:pk>/', user_about, name='user_about'),
    path('messages/<int:pk>/', message_view, name='message_view'),
    path('message_delete/<int:pk>/', message_delete, name='message_delete'),
    path('message_update/<int:pk>/', message_update, name='message_update'),
    path('create_post/', create_post, name='create_post'),
    path('delete_post/', delete_post, name='delete_post'),
    path('post_update/', post_update, name='post_update'),
    path('create_comment/<int:post_id>/', create_comment, name='create_comment'),
    path('delete_comment/<int:post_id>/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('feed/', feed_view, name='feed'),
    path('like/<int:post_id>', like_view, name='like'),
    path('dislike/<int:post_id>', dislike_view, name='dislike')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


