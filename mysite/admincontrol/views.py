from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from catalog.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
# Create your views here.
def index(request):
    context = {
        "title": "List",
    }

    return render(request, "addproduct-admin.html", context)

@csrf_exempt
def showdata (request):
    if request.method == "POST":
        Pid = request.POST.get("Pid", "")
        Pname = request.POST.get("Pname", "")
        Pbrand = request.POST.get("Pbrand", "")
        Ppicture = request.POST.get("Ppicture", "")
        Pprice = request.POST.get("Pprice", "")
        Ptype = request.POST.get("Ptype", "")
        Pamount = request.POST.get("Pamount", "")
        Pdetail = request.POST.get("Pdetail", "")
        print Pid
        print Pname
        print Pbrand
        print Ppicture
        print Pprice
        print Ptype
        print Pamount
        print Pdetail

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO product (Pid, Pname, Pbrand, Ppicture, Pprice, Ptype, Pamount, Pdetail) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (Pid, Pname, Pbrand, Ppicture, Pprice, Ptype, Pamount, Pdetail))
            #cursor.execute("INSERT INTO person (firstname, lastname, middlename, gender, dateofB) VALUES (%s, %s, %s, %s, %s)", (firstName, lastName, midName, gender, dateOfBirth))

        # cursor.execute("DELETE FROM login_users where id= %s", user_id)
    
        # row = cursor.fetchone()


    return HttpResponseRedirect('/catalog/select/')

def select (request):
    row = Product.objects.all()    
    context = {
        "rowlist": row, 
        "title": "List",
        }

    # message = 'xxxx'

    return render(request, "select.html", context)

def update(request):
    _id = request.GET.get('id','')
    productlist = Product.objects.filter(id=_id)
    context = {
        "productlist": productlist, 
        "title": "List",
    }
        
    return render(request,"update.html",context)

@csrf_exempt
def doUpdate (request):
    if request.method == "POST":
        _id = request.POST.get("id", "")
        Pid = request.POST.get("Pid", "")
        Pname = request.POST.get("Pname", "")
        Pbrand = request.POST.get("Pbrand", "")
        Ppicture = request.POST.get("Ppicture", "")
        Pprice = request.POST.get("Pprice", "")
        Ptype = request.POST.get("Ptype", "")
        Pamount = request.POST.get("Pamount", "")
        Pdetail = request.POST.get("Pdetail", "")
        print Pid
        print Pname
        print Pbrand
        print Ppicture
        print Pprice
        print Ptype
        print Pamount
        print Pdetail

        with connection.cursor() as cursor:
            cursor.execute("UPDATE product SET Pid = %s, Pname = %s, Pbrand = %s, Ppicture = %s, Pprice = %s, Ptype = %s, Pamount = %s, Pdetail = %s WHERE id = %s", (Pid, Pname, Pbrand, Ppicture, Pprice, Ptype, Pamount, Pdetail, _id))

    return HttpResponseRedirect('/catalog/select/')

def delete(request):
    _id = request.GET.get('id','')
    p = Product.objects.get(id = _id)
    p.delete()
    return HttpResponseRedirect('/catalog/select/')