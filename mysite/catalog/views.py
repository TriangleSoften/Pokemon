from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from models import Product
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.db.models import Q
# Create your views here.
@csrf_exempt
def allcatalog(request):
    if(request.method=='GET'):
        _search = request.GET.get('search','')
    else:
        _search = request.POST.get('search','')
    if(_search != ''): 
        queryset = Product.objects.filter(Q(Ptype__icontains=_search) | Q(Pname__icontains=_search) | Q(Pprice__icontains=_search) | Q(Pbrand__icontains=_search) | Q(Pid__icontains=_search))
    else: 
        queryset = Product.objects.all()
    userin=request.user.username
    if (userin == ""):
        logged = 0
    else :
        logged = 1
    context = {
        "object_list": queryset, 
        "title": "List",
        "user": userin,
        "logged": logged,
    }
    return render(request, "catalog.html", context)