from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse


def welcome(request):
	 return render(request, 'welcome.html',  {'got_itin_info': ''})