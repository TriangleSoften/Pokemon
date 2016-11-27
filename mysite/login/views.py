from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from register.models import UserData
from django.views.decorators.csrf import csrf_exempt


def index(request):

	logout(request)
	
	context = {
    "isfail": False,
  }

	return render(request, "login.html", context)

@csrf_exempt
def attempt(request):

  if request.method == "POST":
		useratt = request.POST.get("user", ".")
		passatt = request.POST.get("pwd", ".")
		if not request.POST.get('remember_me', None):
			request.session.set_expiry(0)
		print(useratt)
		print(passatt)

  user = authenticate(username=useratt, password=passatt)
  if user is not None:
		login(request, user)
        # Redirect to a success page.
		return HttpResponseRedirect('/home/')
  else:
        # Return an 'invalid login' error message.
		return HttpResponseRedirect('/login/failattempt/')


def failattempt(request):

  logout(request)
  context = {
    "isfail": True,
  }

  return render(request, "login.html", context)


def forgot(request):

  context = {
    "isfail": False,
  }
  return render(request, "fpwd.html", context)
    

@csrf_exempt
def foratt(request):
  if request.method == "POST":
    useratt = request.POST.get("user", ".")
    email = request.POST.get("email", ".")
    dayBD = request.POST.get("dayBD", "")
    monthBD = request.POST.get("monthBD", "")
    yearBD = request.POST.get("yearBD", "")
    dateofbirth = dayBD +"/"+ monthBD +"/"+ yearBD

    user = User.objects.get(username=useratt)
    udata = UserData.objects.filter(username=useratt)

    for ud in udata:
      print(ud.dateofbirth)
      print(dateofbirth)
      if(ud.dateofbirth==dateofbirth and user.email==email):     
        login(request, user)
        return HttpResponseRedirect('/profile/editpassword/')

      else:
        context = {
        "isfail": True,
        }
        return render(request, "fpwd.html", context)