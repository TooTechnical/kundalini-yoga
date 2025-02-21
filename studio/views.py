from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import YogaClass
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import RegistrationForm
from .forms import ProfileUpdateForm
from .models import Profile
from .models import ForumPost
from .models import Post
from studio.models import Post



# Yoga Detail View
def yoga_detail(request, pk):  

    yoga_class = get_object_or_404(YogaClass, pk=pk)  # Fetch the yoga class by primary key or return 404
    return render(request, 'yoga_detail.html', {'yoga_class': yoga_class})

# Yoga List View with Pagination
def yoga(request):
    yoga_classes = YogaClass.objects.all()  # Fetch all yoga classes from the database
    paginator = Paginator(yoga_classes, 5)  # Show 5 classes per page
    page_number = request.GET.get('page')  # Get the current page number from the URL query string
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object
    return render(request, 'yoga.html', {'page_obj': page_obj})

# Homepage View
def index(request):
    return render(request, 'index.html')  # Render index.html template

# Contact Form View
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email or log it)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # For now, just print the data to the console (you can replace this with email sending logic)
            print(f"Name: {name}, Email: {email}, Message: {message}")

            # Redirect to a success page
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

# Success Page View
def success(request):
    return HttpResponse('Thank you for your message!')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log in the user after registration
            return redirect('index') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    # Ensure the user has a profile (fallback for missing profiles)
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


@login_required
def yoga(request):
    yoga_classes = YogaClass.objects.all()
    return render(request, 'yoga.html', {'yoga_classes': yoga_classes})


def forum(request):
    posts = ForumPost.objects.all()
    return render(request, 'forum/forum.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        ForumPost.objects.create(author=request.user, title=title, content=content)
        return redirect('forum')
    return render(request, 'forum/create_post.html')

@require_POST
def logout_view(request):
    logout(request)
    return redirect('home')  # or wherever you want to redirect after logout

def community_forum(request):
    all_posts = Post.objects.all().order_by('-created_at')
    return render(request, 'forum.html', {'posts': all_posts})