"""crud_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from crud_app.views import HelloView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', include('crud_app.urls')),
    path('',HelloView.as_view()),
    path('api-token-auth/', obtain_jwt_token, name='api_token_auth'),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('authpro/',include('oauth2_provider.urls')),
    path('socia/', include('social_django.urls', namespace='socia'))
]
