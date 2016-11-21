from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render



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
