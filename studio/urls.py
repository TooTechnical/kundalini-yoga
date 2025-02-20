from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Homepage
    path('contact/', views.contact, name='contact'),  # Contact page
    path('success/', views.success, name='success'),  # Success page
    path('yoga/', views.yoga, name='yoga'),          # Yoga list page
    path('yoga/<int:pk>/', views.yoga_detail, name='yoga_detail'),  # Yoga detail page
    path('register/', views.register, name='register'),  # Registration page
    path('profile/', views.profile, name='profile'),  # User profile page
    path('forum/', views.forum, name='forum'),  # Forum page
    path('forum/new/', views.create_post, name='create_post'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),


]
