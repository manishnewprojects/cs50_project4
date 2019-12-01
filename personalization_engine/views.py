from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
import ast, json, datetime, re
from .models import Sight, Restaurant
from django.template.loader import render_to_string
from django.db.models import Q


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

		request.session['user_score'] = int(user_score[0])
		request.session['visit_date'] = visit_date
		request.session['duration']   = int(duration[0])
		request.session['season'] 	  = int(season[0])

		return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def render_itin(request):

	duration = request.session['duration']
	user_score = request.session['user_score']
	
	sights = Sight.objects.filter(Q(min_duration__lte = duration))[:(duration*3)] 

	restaurants = Restaurant.objects.filter(Q(type_score__gte = user_score))[:(duration*3)] 

	day=1

	#while (day <= duration):
	#	print("sight",sights[day], "locality", sights[day].locality )
		#restaurants.update({'restaurant':Restaurant.objects.filter(Q(type_score__gte = user_score) & Q(zone = sights[day].locality) ).distinct()[:1]})
		#itin[1].update({'sight':sights[1], 'restaurant':eating_place})
	#	day+=1
		#print ("got rest", eating_place)
		#restaurants.update(eating_place)
	#for sight in sights:
	#	eating_place = Restaurant.objects.filter(type_score__gte = user_score, zone= sight.locality).distinct()[1]
	#	restaurants.update(eating_place)

 
	#return HttpResponse(html)
	return render(request, 'itin_render.html', {'duration':range(duration), 'sights':sights, 'restaurants':restaurants})

 

 