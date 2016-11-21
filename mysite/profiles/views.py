from django.http import HttpResponse
from django.shortcuts import render
from register.models import UserData
from django.contrib.auth.models import User


def index(request):

	userin=request.user.username
	print (userin)

	queryset = UserData.objects.filter(username=userin)
	fname=request.user.first_name
	lname=request.user.last_name
	em=request.user.email

	print (em)

	context = {
		"user_data": queryset,
		"firstname": fname,
		"lastname": lname,
		"email": em,
	}
	return render(request, "profile.html", context)