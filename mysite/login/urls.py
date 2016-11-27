from django.conf.urls import url

from . import views

urlpatterns = {
	url(r'^$', views.index, name='index'),
	url(r'^attempt/$', views.attempt),
	url(r'^failattempt/$', views.failattempt),
	url(r'^forgot/$', views.forgot),
	url(r'^foratt/$', views.foratt),
}