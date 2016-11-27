from django.conf.urls import url

from . import views

urlpatterns = {
	url(r'^$', views.index),
	url(r'^addToCart/$', views.addToCart),
	url(r'^remove/$', views.remove),
}