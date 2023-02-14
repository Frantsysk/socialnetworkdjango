from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, MessageForm, PostForm, CommentForm
from django.contrib.auth import authenticate, login
from .models import Profile, Friend, Message, Post, Comment, Like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
    message = Message.objects.filter(Q(sender = request.user) | Q(receiver = request.user))
    my_friends = Friend.objects.filter(owner=request.user)
    friends_id = list(map(lambda friend: friend.friends.id, my_friends))
    show_friends = User.objects.filter(id__in = friends_id)
    show_posts = Post.objects.filter(owner = request.user)
    display_users = User.objects.all().exclude(id__in = friends_id).exclude(id = request.user.id)
    context = {'profile': profile, 'users': display_users, 'friends': show_friends, 'message': message, 'posts': show_posts}
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

@login_required(login_url='signup_view')
def delete_friend(request, pk):
    owner = request.user
    friend = User.objects.get(id=pk)
    Friend.objects.filter(owner=owner, friends=friend).delete()
    return redirect('about')


def user_about(request, pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(owner = user)
    show_posts = Post.objects.filter(owner = user)
    my_friends = Friend.objects.filter(owner = user)
    friends_id = list(map(lambda friend: friend.friends.id, my_friends))
    show_friends = User.objects.filter(id__in = friends_id)
    display_users = User.objects.all().exclude(id__in = friends_id).exclude(id = request.user.id)
    context = {'profile': profile, 'users': display_users, 'user': user, 'friends':  show_friends, 'posts': show_posts}
    return render (request, 'NetworkApp/about.html', context)


def message_view(request, pk):
    receiver = User.objects.get(id=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)   
        if form.is_valid():           
            mes = form.save(commit=False)
            mes.sender = request.user
            mes.receiver = receiver
            mes.save()
            return redirect('message_view', pk) 
    message = Message.objects.filter(Q(sender = request.user, receiver = receiver) | Q(sender = receiver, receiver = request.user)).order_by('-date')[:5]
    unread_messages = Message.objects.filter(sender = receiver, read = False, receiver = request.user).update(read = True)
    context = {'form': MessageForm(), 'message': message, 'user_id': pk, 'receiver': receiver}
    return render (request, 'NetworkApp/messages.html', context)


@login_required(login_url='message_view')
def message_delete(request, pk):
    message_id = request.POST.get('message_id')
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect('message_view', pk)


@login_required(login_url='message_view')
def message_update(request, pk):
    update_status = True
    message_id = request.POST.get('message_id')
    message = Message.objects.get(id=message_id)
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            form.save()
            return redirect('message_view', pk)
    context = {'form': MessageForm(instance=message), 'user_id': pk, 'update_status': update_status}
    return render(request, 'NetworkApp/messages.html', context)

@login_required(login_url='about')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('about')
    context = {'form': PostForm()}
    return render(request, 'NetworkApp/about.html', context)


@login_required(login_url='about')
def delete_post(request):
    post_id = request.POST.get('post_id')
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('about')


@login_required(login_url='about')
def post_update(request):
    update_status = True
    post_id = request.POST.get('post_id')
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('about')
    context = {'form': PostForm(instance=post), 'update_status': update_status, 'post_id': post_id}
    return render(request, 'NetworkApp/about.html', context)


def create_comment(request, post_id):
    post = Post.objects.get(id = post_id)
    user_id = post.owner.id
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user
            comment.post = Post.objects.get(id=post_id)
            comment.save()
            return redirect('user_about', user_id)
    context = {'form': CommentForm(), 'post_id': post_id, 'comment_page': True}
    return render(request, 'NetworkApp/about.html', context)


def delete_comment(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    user_id = post.owner.id
    comment = Comment.objects.get(id=comment_id)
    if request.user == post.owner or request.user == comment.owner:
        comment.delete()
    return redirect('user_about', user_id)


def feed_view(request):
    friend_connections = Friend.objects.filter(owner = request.user)
    friends = list(map(lambda friend: friend.friends, friend_connections))
    posts = Post.objects.filter(owner__in = friends)
    context = {'posts': posts}
    return render(request, 'NetworkApp/feed.html', context)


def like_view(request, post_id):
    post = Post.objects.get(id=post_id)
    amount = Like.objects.filter(post=post, vote='like').count()
    like = Like(vote='like', user=request.user, post=post)
    like.save()
    return redirect('feed')

def dislike_view(request, post_id):
    pass









