from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from register.models import UserData
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.contrib.auth import authenticate, login, logout



def index(request):

	userin=request.user.username
	print (userin)

	queryset = UserData.objects.filter(username=userin)
	fname=request.user.first_name
	lname=request.user.last_name
	em=request.user.email

	print (em)

	context = {
		"user" :userin,
		"user_data": queryset,
		"firstname": fname,
		"lastname": lname,
		"email": em,
	}
	return render(request, "profile.html", context)

def editpro(request):
	
	userin=request.user.username
	print (userin)

	queryset = UserData.objects.filter(username=userin)
	fname=request.user.first_name
	lname=request.user.last_name
	em=request.user.email

	print (em)

	context = {
		"user" :userin,
		"user_data": queryset,
		"firstname": fname,
		"lastname": lname,
		"email": em,
	}
	return render(request, "editprofile.html", context)

@csrf_exempt
def updatepro(request):

	userin=request.user.username
	print (userin)

	firstname = request.POST.get("firstName", "")
	lastname = request.POST.get("lastName", "")
	phonenum = request.POST.get("phone", "")
	address = request.POST.get("address","")

	user = User.objects.get(username=userin)
	user.first_name = firstname
	user.last_name = lastname
	user.save()
	with connection.cursor() as cursor:
		cursor.execute("UPDATE userdata SET phonenum = %s, address = %s WHERE username = %s", (phonenum, address, userin))


	return HttpResponseRedirect('/profile')

def editpass(request):

	userin=request.user.username
	context = {
		"user" :userin,
		"isfail": False,
	}
	return render(request, "editpassword.html", context)

@csrf_exempt
def updatepass(request):

	userin=request.user.username
	print (userin)

	pass1 = request.POST.get("pwd", "")
	pass2 = request.POST.get("pwd2", "")

	if pass1!=pass2:
		context = {
		"isfail": True,
		}
		return render(request, "editpassword.html", context)

	user = User.objects.get(username=userin)
	user.set_password(pass1)
	user.save()

	user = authenticate(username=userin, password=pass1)
	login(request, user)
	
	return HttpResponseRedirect('/profile')