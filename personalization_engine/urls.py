from django.urls import path

from . import views
 

urlpatterns = [	

 	path('profile_builder', views.profile_builder, name='profile_builder'),

]