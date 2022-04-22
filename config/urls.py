"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 



schema_view = get_schema_view( 
    openapi.Info(
        title="ToDo Task Manager API",
        default_version="v1",
        description="A personal task management app for professionals in the workforce. The project aimed to build a task management app that improves productivity of individuals at work. The goal is to design a task management app that combines a simple user interface with an easy user experience.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="adekoyatunde101@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todo/', include('todos.urls')),
    path('api/permission/', include('rest_framework.urls')),
    path('api/authentication/', include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui( 'redoc', cache_timeout=0), name='schema-redoc'),
]
