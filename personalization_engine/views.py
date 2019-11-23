from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
import ast, json, datetime, re
 
# Create your views here.
#@csrf_exempt
def check_dates(request):
	if request.method == 'POST':
		if (request.POST.get('trip_length') !=0 ):
			#print("got1", request.POST)
			request.session['trip_date']= request.POST.get('trip_date')
			request.session['trip_season']= request.POST.get('trip_season')
			request.session['trip_length'] =request.POST.get('trip_length')

			#print("got1.5", request.POST.get('trip_length'))
			#print("got2", request.session['trip_season'])
			return HttpResponse('success') # if everything is OK
		else:
			return HttpResponse('FAIL!!!!!')
	return render(request, 'profile_builder.html')

def profile_builder(request):
	return render(request, 'profile_builder.html')


def itin_builder(request):
	if request.method == 'POST':
		visit_date=json.dumps(request.POST.get('arr_date'))
		user_score=json.dumps(request.POST.get('user_score'))
		duration  =json.dumps(request.POST.get('duration'))
		season    =json.dumps(request.POST.get('season'))

		user_score=re.findall('\d+', user_score)
		duration  =re.findall('\d+', duration)
		season    =re.findall('\d+', season)

		match = re.search('\d{2}/\d{2}/\d{4}', visit_date)
		vist_date = datetime.datetime.strptime(match.group(), '%m/%d/%Y').date()

		print("user info got", user_score[0],"++",duration[0],"---",season[0],"===","[[[", visit_date)
		
		
		return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

	return render(request, 'itin_builder.html')


 