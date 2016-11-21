from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^editprofile/$', views.editpro),
	url(r'^editpassword/$', views.editpass),
	url(r'^updatepro/$', views.updatepro),
	url(r'^updatepass/$', views.updatepass),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]




