from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from models import *
from catalog.models import *

def index(request):
	userin=request.user.username
	if(userin ==""):
		return HttpResponseRedirect('/login/')
	cart = CartItem.objects.filter(username=userin)
	cartitem = Product.objects.none()
	item = list(cartitem)
	for obj in cart:
		_p = Product.objects.get(Pid=obj.Pid)
		item.append(_p)
	if (userin == ""):
		logged = 0
	else :
		logged = 1
	context = {
		"object_list": item, 
		"title": "List",
		"user": userin,
		"logged": logged,
	}
	return render(request, "cart.html", context)

@csrf_exempt
def addToCart(request):
	userin=request.user.username
	if(userin == ""):
		return HttpResponseRedirect('/login/')
	_Pid = request.GET.get('Pid','')
	try :
		cartitem =  CartItem.objects.get(username=userin,Pid=_Pid)
	except:
		cartitem =  CartItem(username=userin,Pid=_Pid,Pamount = 1)
		cartitem.save()
	return HttpResponseRedirect('/cart/')

@csrf_exempt
def remove(request):
	userin=request.user.username
	if(userin == ""):
		return HttpResponseRedirect('/login/')
	_Pid = request.GET.get('Pid','')
	try :
		cartitem =  CartItem.objects.get(username=userin,Pid=_Pid)
		cartitem.delete()
	except :
		return HttpResponseRedirect('/cart/')
	return HttpResponseRedirect('/cart/')