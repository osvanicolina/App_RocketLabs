# -*- coding: utf-8 necessary for django string usage -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

app_name = 'bundles_app'

urlpatterns = [
    url(r'^services/new$', views.service_create_view, name = "create_service"),
    url(r'^services/$', views.all_services_view, name = "all_services"),
    url(r'^services/([0-9]+)/$', views.service_detail_view, name = "detail_service"),
    url(r'^services/([0-9]+)/edit$', views.service_edit_view, name = "edit_service"),
    url(r'^bundles/client/new$', views.create_custom_bundle_view, name = "create_custom_bundle"),
    url(r'^bundles/new$', views.create_bundle_view, name = "create_bundle"),
]