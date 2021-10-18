"""ipam_poc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from openwisp_users.api.urls import get_api_urls as get_users_api_urls

urlpatterns = [
    # admin URLs
    path('admin/', admin.site.urls),
    # IPAM API
    path('', include('openwisp_ipam.urls')),
    # OpenAPI docs
    path('api/v1/', include('openwisp_utils.api.urls')),
    # Bearer Authentication API URL
    url(r'^api/v1/', include((get_users_api_urls(), 'users'), namespace='users')),
]
