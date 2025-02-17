"""
URL configuration for jerima_club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from authentication import urls as auth_urls
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('classes/', include('classes_programs.urls')),
    path('events/', include('events.urls')),
    path('membership/', include('membership.urls')),
    path('gallery/', include('gallery.urls')),
    path('blog/', include('blog.urls')),
    path('store/', include('store.urls')),
    path('contact/', include('contact.urls')),
    path('member/', include('member_portal.urls')),
    path('dashboard/', include('admin_dashboard.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('authentication/', include(auth_urls)),  # Include authentication app's URLs
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout view
]

if settings.DEBUG:
    # Serve static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Serve media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)