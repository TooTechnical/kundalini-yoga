from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import ContactForm, RegistrationForm, ProfileUpdateForm
from .models import YogaClass, Profile, ForumPost, Post
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Yoga Detail View
def yoga_detail(request, pk):  
    yoga_class = get_object_or_404(YogaClass, pk=pk)
    return render(request, 'yoga_detail.html', {'yoga_class': yoga_class})

# Yoga List View with Pagination (Single Implementation)
def yoga(request):
    yoga_classes = YogaClass.objects.all().order_by('date')
    paginator = Paginator(yoga_classes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'yoga.html', {'page_obj': page_obj})

# Homepage View
def index(request):
    return render(request, 'index.html')

# Contact Form View
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Success Page View
def success(request):
    return HttpResponse('Thank you for your message!')

# Registration View
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Profile View
@login_required
def profile(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
        
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})

# Forum Views
def forum(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    return render(request, 'forum/forum.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        ForumPost.objects.create(
            author=request.user,
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('forum')
    return render(request, 'forum/create_post.html')

# Logout View
@require_POST
def logout_view(request):
    logout(request)
    return redirect('index')

# Community Forum View (Consolidated)
def community_forum(request):
    all_posts = Post.objects.all().order_by('-created_at')
    return render(request, 'forum.html', {'posts': all_posts})
