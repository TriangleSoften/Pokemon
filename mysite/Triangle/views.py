from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_list(request): #list items
	userin=request.user.username
	print("hello")
	print(userin)
	if (userin == ""):
		logged = 0
	else :
		logged = 1
	context = {
		"title": "List",
		"user": userin,
		"logged": logged,
	}
	return render(request, "codeboost.html", context)