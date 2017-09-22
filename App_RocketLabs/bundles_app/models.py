# -*- coding: utf-8 necessary for django string usage -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

"""""""""""""""""""""""""""
Service Model

"""""""""""""""""""""""""""
class Service(models.Model):



	name = models.CharField(max_length = 50)
	about = models.TextField(max_length = 255)
	visual_aid = models.ImageField(blank = True, null =True)
	service_fee = models.DecimalField(max_digits = 3, decimal_places = 2, blank = True, null = True)
	is_active = models.BooleanField(default = True)

	def __str__(self):
		return self.name

"""""""""""""""""""""""""""
Bundle Model

"""""""""""""""""""""""""""
class Bundle(models.Model):
	
	services = models.ManyToManyField(Service)

	title = models.CharField(max_length = 100, unique=True)
	about = models.TextField(max_length=255)
	bundle_extra_fee = models.DecimalField(max_digits=4, decimal_places = 2, blank = True, null = True)
	bundle_total_fee = models.DecimalField(max_digits=4, decimal_places= 2, blank = True, null = True)
	is_custom = models.BooleanField()
	is_active = models.BooleanField(default = True)

	def __str__(self):
		return self.title



