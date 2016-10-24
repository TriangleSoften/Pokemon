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