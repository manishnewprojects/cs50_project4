"""visit_sf URL Configuration

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
from . import views

admin.site.site_header = "SF Personalized Itinerary"
admin.site.site_title  = "SF Personalized Itinerary "
admin.site.index_title = "Welcome to SF Personalized Itinerary Admin"


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),     
    path('personalization_engine/', include('personalization_engine.urls')),

    #path('users/', include('users.urls')),  
    #path('itin/', include('itin.urls')),

]
