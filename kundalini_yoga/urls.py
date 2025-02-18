from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Admin panel route
    path('', include('studio.urls')),         # Include app-level URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs (login/logout)
]
