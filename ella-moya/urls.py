"""ella-moya URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Keep for Django admin if needed
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    # Removed: profiles, bag, checkout, allauth URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
