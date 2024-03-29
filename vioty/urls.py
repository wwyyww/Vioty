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
   
    path('', map.views.index, name='index' ),
    path('login/', map.views.login, name='login'),
    path('signup/', map.views.signup, name='signup'),
    path('camera/', map.views.camera, name='camera'),
    path('main_new/', map.views.main_new, name='main_new'),
    path('main_new/sub_map/', map.views.sub_map, name='sub_map'),
    path('main_new/sub_cctv/', map.views.sub_cctv, name='sub_cctv'),
    path('main_new/sub_record/', map.views.sub_record, name='sub_record'),
    path('main_new/sub_setting/', map.views.sub_setting, name='sub_setting'),
    path('main_new/sub_planning/', map.views.sub_planning, name='sub_planning'),
    path('main_new/sub_stats/', map.views.sub_stats, name='sub_stats'),
    path('main_new/IdPopup/', map.views.IdPopup, name='IdPopup'),
    path('main_new/PwPopup/', map.views.PwPopup, name='PwPopup'),
    
    

]
