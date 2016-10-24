from django.http import HttpResponse
from django.shortcuts import render
from models import Product

# Create your views here.
def allcatalog(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset, 
		"title": "List",
	}
	return render(request, "catalog.html", context)

def skincare(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset, 
		"title": "List",
	}
	return render(request, "Skincare.html", context)

def base_makeup(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset, 
		"title": "List",
	}
	return render(request, "base_makeup.html", context)

def point_makeup(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset, 
		"title": "List",
	}
	return render(request, "point_makeup.html", context)

def accessories(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset, 
		"title": "List",
	}
	return render(request, "accessories.html", context)

def fragrance(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset, 
		"title": "List",
	}
	return render(request, "fragrance.html", context)