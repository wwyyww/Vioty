"""vioty URL Configuration

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
from django.contrib import admin
from django.urls import path, include
import map.views

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', map.views.main, name='main' ),
    path('login/', map.views.login, name='login'),
    path('signup/', map.views.signup, name='signup'),
    path('camera/', map.views.camera, name='camera'),
    path('index/', map.views.index, name='index'),
    path('main_new/', map.views.main_new, name='main_new'),

]
