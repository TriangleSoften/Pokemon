from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from register.models import UserData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render


def index(request):
  userin=request.user.username
  print (userin)
  
  context = {
    "failmsg": "",
  }

  return render(request, "register.html", context)


@csrf_exempt
def attempt (request):
    if request.method == "POST":
        firstname = request.POST.get("firstName", "")
        lastname = request.POST.get("lastName", "")
        username = request.POST.get("username", "")
        password = request.POST.get("pwd", "")
        password2 = request.POST.get("pwd2", "")
        email = request.POST.get("email","")
        email2 = request.POST.get("email2","")
        gender = request.POST.get("gender", "")
        phonenum = request.POST.get("phone", "")
        dayBD = request.POST.get("dayBD", "")
        monthBD = request.POST.get("monthBD", "")
        yearBD = request.POST.get("yearBD", "")

        dateofbirth = dayBD +"/"+ monthBD +"/"+ yearBD

        print firstname
        print lastname
        print username
        print email
        print gender
        print dateofbirth
        print phonenum

        if(password!=password2):
        	return HttpResponseRedirect('/register/failattempt/?id=pass')

        if(email!=email2):
        	return HttpResponseRedirect('/register/failattempt/?id=email')

        try:
        	user = User.objects.get(username = username)
        	return HttpResponseRedirect('/register/failattempt/?id=user')
        except :
        	print ""


        try:
        	user = User.objects.get(email = email)
        	return HttpResponseRedirect('/register/failattempt/?id=email2')
        except :
        	print ""

        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        with connection.cursor() as cursor:
           	cursor.execute("INSERT INTO userdata (username, gender, dateofbirth, phonenum) VALUES (%s, %s, %s, %s)", (username, gender, dateofbirth, phonenum))

        login(request, user)
    return HttpResponseRedirect('/home/')


def failattempt (request):

  userin=request.user.username
  print (userin)

  _id = request.GET.get('id','')
  msg = ""

  if _id == 'pass':
    msg = "Both password must be the same"
  elif _id == 'email':
    msg = "Both email must be the same"
  elif _id == 'user':
    msg = "Username already in use"
  elif _id == 'email2':
    msg = "Email already in use"

  context = {
    "failmsg": msg,
  }

  return render(request, "register.html", context)