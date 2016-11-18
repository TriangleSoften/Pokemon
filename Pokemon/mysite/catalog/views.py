from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from models import Product

# Create your views here.
def allcatalog(request):
	_search = request.GET.get('search','')
	if(_search != ''): 
		queryset = Product.objects.filter(Ptype=_search)
	else: 
		queryset = Product.objects.all()
	context = {
		"object_list": queryset, 
		"title": "List",
	}
	return render(request, "catalog.html", context)
def index(request):
	message = '''<html>
                    <head>
                        <style>
                            body {
                                margin: 0;
                                padding: 0;
                            }

                            .container {
                                position: relative;
                                width: 100%;
                            }

                        </style>
                    </head>
                    <body>
                    <a href="../../home">Home</a>

                        <div class="container">
                            <form name="submit_form" id="submit_form" action="/catalog/showdata/" method="post">
                                <table border="1" style="width: 400px; margin-left: auto; margin-right: auto; margin-top: 30px;" cellpadding="8" cellspacin="8">
                                    <tr>
                                    	<td style="width: 30%; text-align: center;">
                                    		Product ID
                                    	</td>
                                    	<td>
                                    		<input type="text" name="Pid" value="" placeholder="Please enter product ID." style="width: 100%; height: 30px;" />
                                    	</td>
                                    </tr>
                                    <tr>
                                    	<td style="width: 30%; text-align: center;">
                                    		Product Name
                                    	</td>
                                    	<td>
                                    		<input type="text" name="Pname" value="" placeholder="Please enter product name." style="width: 100%; height: 30px;" />
                                    	</td>
                                    </tr>
                                    <tr>
                                    	<td style="width: 30%; text-align: center;">
                                    		Product brand
                                    	</td>
                                    	<td>
                                    		<input type="text" name="Pbrand" value="" placeholder="Please enter product brand." style="width: 100%; height: 30px;" />
                                    	</td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Product Picture
                                        </td>
                                        <td>
                                            <input type="text" name="Ppicture" value="" placeholder="Please enter link of product picture." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Product Price
                                        </td>
                                        <td>
                                            <input type="text" name="Pprice" value="" placeholder="Please enter product price." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Product Type
                                        </td>
                                        <td>
                                            <input type="radio" name="Ptype" value="SkinCare" checked /> SkinCare
                                            <br />
                                            <input type="radio" name="Ptype" value="BaseMakeup" /> Base Makeup
                                            <br />
                                            <input type="radio" name="Ptype" value="PointMakeup" /> Point Makeup
                                            <br />
                                            <input type="radio" name="Ptype" value="Accessories" /> Accessories
                                            <br />
                                            <input type="radio" name="Ptype" value="Fragrance" /> Fragrance
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Product Amount
                                        </td>
                                        <td>
                                            <input type="number" min="0" name="Pamount"/>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Product Detail
                                        </td>
                                        <td>
                                            <input type="text" name="Pdetail" value="" placeholder="Please enter product detail." style="width: 100%; height: 180px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            &nbsp;
                                        </td>
                                        <td>
                                            <input type="button" value="Cancel" />
                                            <input type="submit" value="Submit" />
                                        </td>
                                    </tr>
                                </table>
                            </form>
                        </div>
                    </body>
                </html>'''

	return HttpResponse (message)

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

    user = ''
    for row in Product.objects.raw('SELECT * FROM product'):
    	print(row.id)
        print(row.Pid)
        print(row.Pname)
        print(row.Pbrand)
        print(row.Ppicture)
        print(row.Pprice)
        print(row.Ptype)
        print(row.Pamount)
        print(row.Pdetail)
      	user += '''
                <tr>
                    <td>'''+str(row.id)+'''</td>
                    <td>'''+row.Pid+'''</td>
                    <td>'''+row.Pname+'''</td>
                    <td>'''+row.Pbrand+'''</td>
                    <td>'''+row.Ppicture+'''</td>
                    <td>'''+str(row.Pprice)+'''</td>
                    <td>'''+row.Ptype+'''</td>
                    <td>'''+str(row.Pamount)+'''</td>
                    <td>'''+row.Pdetail+'''</td>
                    <td><a href="/catalog/update/?id='''+str(row.id)+'''">Update</a></td>
                    <td><a href="/catalog/delete/?id='''+str(row.id)+'''">Delete</a></td>
                </tr>
                '''
    

    message = """<html>
                    <head>
                        <style>
                            body {
                                margin: 0;
                                padding: 0;
                            }

                            .container {
                                position: relative;
                                width: 100%;
                            }

                        </style>
                    </head>
                    <body>
                    <a href="../../home">Home</a>

                        <div class="container">
                            <table border="1" width="800" style="margin-left: auto; margin-right: auto; margin-top: 30px;">
                                """+user+"""
                            </table>
                        </div>
                    </body>
                </html>"""

    # message = 'xxxx'

    return HttpResponse(message)

def update(request):
    _id = request.GET.get('id','')

    row = Product.objects.filter(id=_id)
    product = row[0]
    SkinCareSelected = ''
    if product.Ptype == 'SkinCare':
        SkinCareSelected = 'checked'

    BaseMakeupSelected = ''
    if product.Ptype == 'BaseMakeup':
        BaseMakeupSelected = 'checked'

    PointMakeupSelected = ''
    if product.Ptype == 'PointMakeup':
        PointMakeupSelected = 'checked'
        
    AccessoriesSelected = ''
    if product.Ptype == 'Accessories':
        Accessories = 'checked'
        
    FragranceSelected = ''
    if product.Ptype == 'Fragrance':
        FragranceSelected = 'checked'



    message = '''<html>
                    <head>
                        <style>
                            body {
                                margin: 0;
                                padding: 0;
                            }

                            .container {
                                position: relative;
                                width: 100%;
                            }

                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <form name="submit_form" id="submit_form" action="/catalog/doUpdate/" method="post">
                                <input type="hidden" name="id" value="'''+str(product.id)+'''" />
                                <table border="1" style="width: 400px; margin-left: auto; margin-right: auto; margin-top: 30px;" cellpadding="8" cellspacin="8">
                                    <tr>
                                    	<td style="width: 30%; text-align: center;">
                                    		Product ID
                                    	</td>
                                    	<td>
                                    		<input type="text" name="Pid" value="'''+product.Pid+'''" placeholder="Please enter product ID." style="width: 100%; height: 30px;" />
                                    	</td>
                                    </tr>
                                    <tr>
                                    	<td style="width: 30%; text-align: center;">
                                    		Product Name
                                    	</td>
                                    	<td>
                                    		<input type="text" name="Pname" value="'''+product.Pname+'''" placeholder="Please enter product name." style="width: 100%; height: 30px;" />
                                    	</td>
                                    </tr>
                                    <tr>
                                    	<td style="width: 30%; text-align: center;">
                                    		Product brand
                                    	</td>
                                    	<td>
                                    		<input type="text" name="Pbrand" value="'''+product.Pbrand+'''" placeholder="Please enter product brand." style="width: 100%; height: 30px;" />
                                    	</td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Product Picture
                                        </td>
                                        <td>
                                            <input type="text" name="Ppicture" value="'''+product.Ppicture+'''" placeholder="Please enter link of product picture." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Product Price
                                        </td>
                                        <td>
                                            <input type="text" name="Pprice" value="'''+str(product.Pprice)+'''"  placeholder="Please enter product price." style="width: 100%; height: 30px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Product Type
                                        </td>
                                        <td>
                                            <input type="radio" name="Ptype" value="SkinCare" '''+SkinCareSelected+''' /> SkinCare
                                            <br />
                                            <input type="radio" name="Ptype" value="BaseMakeup" '''+BaseMakeupSelected+'''/> Base Makeup
                                            <br />
                                            <input type="radio" name="Ptype" value="PointMakeup" '''+PointMakeupSelected+'''/> Point Makeup
                                            <br />
                                            <input type="radio" name="Ptype" value="Accessories" '''+AccessoriesSelected+'''/> Accessories
                                            <br />
                                            <input type="radio" name="Ptype" value="Fragrance" '''+FragranceSelected+'''/> Fragrance
                                        </td>
                                    </tr>                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Product Amount
                                        </td>
                                        <td>
                                            <input type="number" value="'''+str(product.Pamount)+'''" min="0" name="Pamount"/>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            Product Detail
                                        </td>
                                        <td>
                                            <input type="text" name="Pdetail" value="'''+product.Pdetail+'''" placeholder="Please enter product detail." style="width: 100%; height: 180px;" />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="width: 30%; text-align: center;">
                                            &nbsp;
                                        </td>
                                        <td>
                                            <input type="button" value="Cancel" />
                                            <input type="submit" value="Submit" />
                                        </td>
                                    </tr>
                                </table>
                            </form>
                        </div>
                    </body>
                </html>'''

    return HttpResponse (message)

@csrf_exempt
def doUpdate (request):
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
            cursor.execute("UPDATE product SET Pid = %s, Pname = %s, Pbrand = %s, Ppicture = %s, Pprice = %s, Ptype = %s, Pamount = %s, Pdetail = %s WHERE id = %s", (Pid, Pname, Pbrand, Ppicture, Pprice, Ptype, Pamount, Pdetail, _id))

    return HttpResponseRedirect('/catalog/select/')

def delete(request):
    _id = request.GET.get('id','')
    with connection.cursor() as cursor:
         cursor.execute("DELETE FROM product where id= %s", _id)
         
    return HttpResponseRedirect('/catalog/select/')