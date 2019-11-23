from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Sight(models.Model):
	title 		= models.CharField(max_length = 100, blank=True, null=True)
	url   		= models.CharField(max_length = 100, blank=True, null=True)
	address 	= models.CharField(max_length = 100, blank=True, null=True)
	locality	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	season 		= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	timeofday 	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	min_duration = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	type_score 	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.title}, {self.url}"


class Restaurant(models.Model):
	name 		= models.CharField(max_length = 100, blank=True, null=True)
	yelp_link   = models.CharField(max_length = 100, blank=True, null=True)
	locality	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	timeofday 	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	type_score 	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.name}, {self.yelp_link}"