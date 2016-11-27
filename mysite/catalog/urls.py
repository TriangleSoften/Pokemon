from django.conf.urls import url
from django.contrib import admin

from views import *

urlpatterns = [
	url(r'^$', allcatalog),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
    url(r'^addproduct/$', index, name='Index'),
	url(r'^showdata/$', showdata),
	url(r'^select/$', select),
	url(r'^update/$', update),
	url(r'^doUpdate/$', doUpdate),
	url(r'^delete/$', delete),
]




