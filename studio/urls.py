from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Homepage
    path('contact/', views.contact, name='contact'),  # Contact page
    path('success/', views.success, name='success'),  # Success page
    path('yoga/', views.yoga, name='yoga'),          # Yoga list page
    path('yoga/<int:pk>/', views.yoga_detail, name='yoga_detail'),  # Yoga detail page
]
