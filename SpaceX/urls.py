"""
URL configuration for SpaceX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path, include
from django.conf import settings
from .views import APIRootView

# Base URL patterns (always available)
urlpatterns = [
    path("", APIRootView.as_view(), name='api-root'),
]

# Conditionally add app URLs based on IS_AVAILABLE setting
if settings.IS_AVAILABLE:
    urlpatterns += [
        path("stats/", include('apps.stats.urls')),
        path("upcoming/", include('apps.upcoming.urls')),
        path("launches/", include('apps.launches.urls')),
        path("dragon/", include('apps.dragon.urls')),
    ]
