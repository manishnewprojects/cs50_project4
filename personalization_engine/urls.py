from django.urls import path

from . import views
 

urlpatterns = [	

 	path('check_dates', views.check_dates, name='check_dates'),
 	path('profile_builder', views.profile_builder, name='profile_builder'),
 	path('itin_builder', views.itin_builder, name='itin_builder'),

]