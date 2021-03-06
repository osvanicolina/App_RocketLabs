# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# imports de modelos de otras apps.
#from core_app.models import Profile
#from bundles_app.models import Bundle

# Create your models here.


def screenshot_directory_path(instance, filename):
    # El screenshot será subido a MEDIA_ROOT/project/<id>/<filename>
    return 'project_screenshots/{0}/{1}'.format(instance.project.id, filename)


"""""""""""""""""""""""""""
Project Model

"""""""""""""""""""""""""""
class Project(models.Model):

	owner_profiles = models.ManyToManyField('core_app.Profile', db_table ="projects_app_owner_profiles")
	bundle = models.ForeignKey('bundles_app.Bundle', null=True, default=None) # Null, blank y default solo para probar mientras no hay bundles implementados.

	title = models.CharField(max_length=100)
	description = models.TextField(max_length=500, default='')
	str_duration = models.CharField(max_length=50, blank = True,default='')
	done_percentage = models.SmallIntegerField(default=0)
	current_stage = models.CharField(max_length=50, blank =True,default='Pre-aprobación.')
	is_complete = models.BooleanField(default = False)
	owner_comment = models.TextField(max_length = 500, blank =True, default='')
	demo_link = models.CharField(max_length = 100, blank = True, default='')
	last_update_date = models.DateTimeField(auto_now=True)
	start_date = models.DateTimeField(auto_now_add=True)
	finish_date = models.DateTimeField(blank = True, null=True, default=None)

	def __str__(self):
		return self.title#.encode('utf-8', errors='replace')

	def get_preview_screenshot(self):
		return self.screenshot_set.get(is_preview=True)

	def get_clients_string(self):
		profiles = self.owner_profiles.all()
		client_string = profiles.first().company_name
		if profiles.count() > 1:
			for profile in profiles[1:]:
				client_string += ", {}".format(profile.company_name)
		return client_string


"""""""""""""""""""""""""""
Screenshot Model

"""""""""""""""""""""""""""
class Screenshot(models.Model):

	class Meta:
		ordering = ['date_uploaded']

	project = models.ForeignKey(Project, null=True, default=None, blank=True, on_delete=models.CASCADE)

	name = models.CharField(max_length=50)
	img = models.ImageField( upload_to = screenshot_directory_path )
	is_preview = models.BooleanField(default=False)
	date_uploaded = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return "{} | {}".format(self.project.title , self.name)#.encode('utf-8', errors='replace')

	def mark_as_only_preview(self):
		screens = Screenshot.objects.filter(project=self.project)
		for screen in screens:
			screen.is_preview = False
			screen.save()
		self.is_preview = True
		self.save()
