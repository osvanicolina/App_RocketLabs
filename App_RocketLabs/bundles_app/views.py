# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from bundles_app.models import Bundle, Service
import bundles_app.forms as bundle_forms
from  bundles_app.forms import CreateServiceForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.


#Vista para crear servicio
def create_service_view(request):
	form = bundle_forms.CreateServiceForm(request.POST or None)
	if request.POST and form.is_valid():
		form.save()
		return HttpResponseRedirect('/')
 	else:
 		form = bundle_forms.CreateServiceForm()
 		return render(request, 'bundles_app/createservice.html', {'form': form ,})



def services_view(request):
	"""
	Esta view le pasa a la template todos los objetos Service.
	"""
	services = Service.objects.all()
	return render(request, 'bundles_app/services.html', {'services': services} )


def detailservice_view (request, service_pk):
	"""
	Esta view le pasa a la template el objeto Service indicado.
	"""
	service_detail = get_object_or_404(Service, pk = service_pk)
	return render(request, 'bundles_app/servicedetail.html', {'service_detail': service_detail})


def editservice_view(request, service_pk):
	if request.method == 'POST':	
		service = get_object_or_404(Service, pk = service_pk)
		form = bundle_forms.CreateServiceForm(request.POST, instance = service, prefix='editservice')
		if form.is_valid():
			form.save()
			messages.success(request, 'Se han guardado los cambios en el servicio con exito')
			return HttpResponseRedirect('/services/'+str(service.id))

	else:
		service = get_object_or_404(Service, pk = service_pk)
		form = bundle_forms.CreateServiceForm(instance = service ,prefix='editservice')
		return render(request, 'bundles_app/editservice.html', {'form':form} )

