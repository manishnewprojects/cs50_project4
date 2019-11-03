from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import ast, json

# Create your views here.
#@csrf_exempt
def profile_builder(request):
	if request.method == 'POST':
		print("requst1", request.POST)

		print("requst2", request.POST.get('trip_duration'))
		user_profile=ast.literal_eval(json.dumps(request.POST))
		print("requst3", user_profile)

		#if 'user_profile' in request.POST:
		#	user_profile = request.POST['user_profile']
		#	print("got")
		#	return HttpResponse('success') # if everything is OK
	return HttpResponse('FAIL!!!!!')
