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



def index(request):
    message = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Cabin+Condensed|PT+Sans+Caption|Viga" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="../../static/css/admintheme.css">
    
    <link rel="shortcut icon" type="image/png" href="../../static/img/Triangle-LOGO_I.png" />
    <title>Administer - TRIANGLE</title>    
</head>

<body>
    
    <!--navbar-->
    <div class="container-fluid">
        <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-header">
                <a class="navbar-brand"><img style="max-width: 200px; margin-top: -10px;" src="../../static/img/Triangle-LOGO_w2.png"></a>
            </div>
            <div class="navbar-right" style="padding-right: 30px;">
                <ul class="nav navbar-nav">
                    <li class="dropdown">
                        <a class="dropdown-toggle" data-toggle="dropdown" href="#">WELCOME ADMIN <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#"><span class="glyphicon glyphicon-new-window"></span>&nbsp&nbspGo to Shop</a></li>
                            <li><a href="#"><span class="glyphicon glyphicon-cog"></span>&nbsp&nbspSetting</a></li>
                            <li><a href="#"><span class="glyphicon glyphicon-log-out"></span>&nbsp&nbspLog out</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </nav>
    </div>

    <!--sidebar-->
    <div class="container-fluid">
        <div class="row content" style="margin-top: 50px;">
            <div class="col-md-2 Sidebar" style="background-color: #563935;padding-top: 2px;margin-bottom: 0px;padding-bottom: 15px;">

                  <div style="margin-top: 40px;">
                  </div>

                <div class="menu-item alpha" style="width:100%;">
                     <h4><a href="home-admin.html"><span class="glyphicon glyphicon-home"></span>&nbsp&nbspHome</a></h4>
                        <p>Welcome Admin!!</p>
                </div>

                <div class="menu-item active active-three-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-briefcase"></span>&nbsp&nbspProduct</a></h4>
                    <ul class="active-sub">
                        <li><a href="./../select/">All Products</a></li>
                        <li><a style="color: #FFA09E;" href="./../addproduct/">Add Product</a></li>
                        <li><a href="#">Out of stock</a></li>
                    </ul>
                </div>

                <div class="menu-item four-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-th-list"></span>&nbsp&nbspOrder</a></h4>
                    <ul class="inactive">
                        <li><a href="#">All Orders</a></li>
                        <li><a href="#">New Orders</a></li>
                        <li><a href="#">Search Order</a></li>
                        <li><a href="#">Create Invoices</a></li>
                    </ul>
                </div>

                <div class="menu-item three-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-tags"></span>&nbsp&nbspPromotion</a></h4>
                    <ul class="inactive">
                        <li><a href="#">All Promotions</a></li>
                        <li><a href="#">Add Promotions</a></li>
                        <li><a href="#">Remove Promotions</a></li>
                    </ul>
                </div>

                <div class="menu-item two-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-user"></span>&nbsp&nbspCustomer</a></h4>
                    <ul class="inactive">
                        <li><a href="#">All Customers</a></li>
                        <li><a href="#">Search Customers</a></li>
                    </ul>
                </div>

                <div class="menu-item two-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-transfer"></span>&nbspShipping</a></h4>
                    <ul class="inactive">
                        <li><a href="#">Shipping Region</a></li>
                        <li><a href="#">Add Region</a></li>
                    </ul>
                </div>

                <div class="menu-item" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-cog"></span>&nbsp&nbspSetting</a></h4>
                </div>

        </div>

            <div class="col-md-10 ">
            <div style="margin-top: 35px;"></div>

            <h2 class="headline">Add Product</h2>
            <hr class="break">
                            <form class="form-horizontal" form name="submit_form" id="submit_form" action="/catalog/showdata/" method="post">
                                <div style="margin-top: 40px;">
                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="ProductID">Product ID</label>
                                        <div class="col-md-3">
                                            <input type="text" name="Pid" value="" placeholder="Please enter product ID." style="width: 100%; height: 30px;" />
                                        </div>
                                    </div> 
                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Name">Name</label>
                                            <div class="col-md-5"> 
                                                <input type="text" name="Pname" value="" placeholder="Please enter product name." style="width: 100%; height: 30px;" />
                                        </div>
                                    </div> 
                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Brand">Brand</label>
                                        <div class="col-md-5">                                             
                                            <input type="text" name="Pbrand" value="" placeholder="Please enter product brand." style="width: 100%; height: 30px;" />
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Price">Price </label>
                                        <div class="col-md-3">          
                                            <input type="text" name="Pprice" value="" placeholder="Please enter product price." style="width: 100%; height: 30px;" />
                                        </div>
                                    </div>


                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Price">Amount </label>
                                        <div class="col-md-3">          
                                            <input type="number" min="0" name="Pamount"/>
                                        </div>
                                    </div>


                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Descript">Description</label>
                                        <div class="col-md-5">
                                            <textarea id="description" rows="10" cols="50" name="Pdetail" value="" placeholder="Please enter product detail."></textarea>
                                            <style>
                                                .userInput {
                                                text-align: left;
                                                margin: 1px;
                                                padding: 1px;
                                                width: 500px;
                                                height: 300px;
                                                vertical-align: top;
                                                }
                                            </style>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Category">Category</label>
                                        <div class="col-md-3"> 
                                            <input type="radio" name="Ptype" value="SkinCare" checked /> SkinCare
                                            <br />
                                            <input type="radio" name="Ptype" value="BaseMakeup" /> Base Makeup
                                            <br />
                                            <input type="radio" name="Ptype" value="PointMakeup" /> Point Makeup
                                            <br />
                                            <input type="radio" name="Ptype" value="Accessories" /> Accessories
                                            <br />
                                            <input type="radio" name="Ptype" value="Fragrance" /> Fragrance
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Image">Product image</label>
                                        <div class="col-md-3">                                                      
                                            <input type="text" name="Ppicture" value="" placeholder="Please enter link of product picture." style="width: 100%; height: 30px; " />
                                        </div>
                                    </div>
                                    
                                    
                                    <div class="form-group">        
                                        <div class="col-md-offset-2 col-md-8 text-size-15">
                                            <input type="button" value="Cancel" />
                                            <input type="submit" value="Submit" />
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>




              </form>
          </div>




        </div>

    </div>

    </div>
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
    

    message = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Cabin+Condensed|PT+Sans+Caption|Viga" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="../../static/css/admintheme.css">
    
    <link rel="shortcut icon" type="image/png" href="../../static/img/Triangle-LOGO_I.png" />
    <title>Administer - TRIANGLE</title> 
    <style>
table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
tr:nth-child(even){background-color: #bfa36d}
</style>  

</head>

<body>
    
    <!--navbar-->
    <div class="container-fluid">
        <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-header">
                <a class="navbar-brand"><img style="max-width: 200px; margin-top: -10px;" src="../../static/img/Triangle-LOGO_w2.png"></a>
            </div>
            <div class="navbar-right" style="padding-right: 30px;">
                <ul class="nav navbar-nav">
                    <li class="dropdown">
                        <a class="dropdown-toggle" data-toggle="dropdown" href="#">WELCOME ADMIN <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#"><span class="glyphicon glyphicon-new-window"></span>&nbsp&nbspGo to Shop</a></li>
                            <li><a href="#"><span class="glyphicon glyphicon-cog"></span>&nbsp&nbspSetting</a></li>
                            <li><a href="#"><span class="glyphicon glyphicon-log-out"></span>&nbsp&nbspLog out</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </nav>
    </div>

    <!--sidebar-->
    <div class="container-fluid">
        <div class="row content" style="margin-top: 50px;">
                <div class="col-md-2 Sidebar" style="background-color: #563935;padding-top: 2px;margin-bottom: 0px;padding-bottom: 15px;">


                  <div style="margin-top: 40px;">
                  </div>

                <div class="menu-item alpha" style="width:100%;">
                     <h4><a href="home-admin.html"><span class="glyphicon glyphicon-home"></span>&nbsp&nbspHome</a></h4>
                        <p>Welcome Admin!!</p>
                </div>

                <div class="menu-item active active-three-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-briefcase"></span>&nbsp&nbspProduct</a></h4>
                    <ul class="active-sub">
                        <li><a style="color: #FFA09E;" href="./../select/">All Products</a></li>
                        <li><a href="./../addproduct/">Add Product</a></li>
                        <li><a href="#">Out of stock</a></li>
                    </ul>
                </div>

                <div class="menu-item four-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-th-list"></span>&nbsp&nbspOrder</a></h4>
                    <ul class="inactive">
                        <li><a href="#">All Orders</a></li>
                        <li><a href="#">New Orders</a></li>
                        <li><a href="#">Search Order</a></li>
                        <li><a href="#">Create Invoices</a></li>
                    </ul>
                </div>

                <div class="menu-item three-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-tags"></span>&nbsp&nbspPromotion</a></h4>
                    <ul class="inactive">
                        <li><a href="#">All Promotions</a></li>
                        <li><a href="#">Add Promotions</a></li>
                        <li><a href="#">Remove Promotions</a></li>
                    </ul>
                </div>

                <div class="menu-item two-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-user"></span>&nbsp&nbspCustomer</a></h4>
                    <ul class="inactive">
                        <li><a href="#">All Customers</a></li>
                        <li><a href="#">Search Customers</a></li>
                    </ul>
                </div>

                <div class="menu-item two-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-transfer"></span>&nbspShipping</a></h4>
                    <ul class="inactive">
                        <li><a href="#">Shipping Region</a></li>
                        <li><a href="#">Add Region</a></li>
                    </ul>
                </div>

                <div class="menu-item" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-cog"></span>&nbsp&nbspSetting</a></h4>
                </div>

        </div>

            <div class="col-md-10">
            <div style="margin-top: 35px;"></div>
            <h2 class="headline">Update and Remove</h2>
            <hr class="break">

                        <div class="container">
                            <table width="800" style="margin-left: auto; margin-right: auto; margin-top: 30px;">
                              <tr>
    <th>Id</th>
    <th>Pid</th>
    <th>Product Name</th>
    <th>Brand</th>
    <th>Picture</th>
    <th>Price</th>
    <th>Type</th>
    <th>Amount</th>
    <th>Detail</th>
    <th></th>
    <th></th>
  </tr>
                                """+user+"""
                            </table>
                        </div>
                        </div>




        </div>

    </div>

    </div>
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



    message = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Cabin+Condensed|PT+Sans+Caption|Viga" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="../../static/css/admintheme.css">
    
    <link rel="shortcut icon" type="image/png" href="../../static/img/Triangle-LOGO_I.png" />
    <title>Administer - TRIANGLE</title>    
</head>

<body>
    
    <!--navbar-->
    <div class="container-fluid">
        <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-header">
                <a class="navbar-brand"><img style="max-width: 200px; margin-top: -10px;" src="../../static/img/Triangle-LOGO_w2.png"></a>
            </div>
            <div class="navbar-right" style="padding-right: 30px;">
                <ul class="nav navbar-nav">
                    <li class="dropdown">
                        <a class="dropdown-toggle" data-toggle="dropdown" href="#">WELCOME ADMIN <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#"><span class="glyphicon glyphicon-new-window"></span>&nbsp&nbspGo to Shop</a></li>
                            <li><a href="#"><span class="glyphicon glyphicon-cog"></span>&nbsp&nbspSetting</a></li>
                            <li><a href="#"><span class="glyphicon glyphicon-log-out"></span>&nbsp&nbspLog out</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </nav>
    </div>

    <!--sidebar-->
    <div class="container-fluid">
        <div class="row content" style="margin-top: 50px;">
            <div class="col-md-2 Sidebar" style="background-color: #563935;padding-top: 2px;margin-bottom: 0px;padding-bottom: 15px;">

                  <div style="margin-top: 40px;">
                  </div>

                <div class="menu-item alpha" style="width:100%;">
                     <h4><a href="home-admin.html"><span class="glyphicon glyphicon-home"></span>&nbsp&nbspHome</a></h4>
                        <p>Welcome Admin!!</p>
                </div>

                <div class="menu-item active active-three-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-briefcase"></span>&nbsp&nbspProduct</a></h4>
                    <ul class="active-sub">
                        <li><a href="./../select/">All Products</a></li>
                        <li><a style="color: #FFA09E;" href="./../addproduct/">Add Product</a></li>
                        <li><a href="#">Out of stock</a></li>
                    </ul>
                </div>

                <div class="menu-item four-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-th-list"></span>&nbsp&nbspOrder</a></h4>
                    <ul class="inactive">
                        <li><a href="#">All Orders</a></li>
                        <li><a href="#">New Orders</a></li>
                        <li><a href="#">Search Order</a></li>
                        <li><a href="#">Create Invoices</a></li>
                    </ul>
                </div>

                <div class="menu-item three-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-tags"></span>&nbsp&nbspPromotion</a></h4>
                    <ul class="inactive">
                        <li><a href="#">All Promotions</a></li>
                        <li><a href="#">Add Promotions</a></li>
                        <li><a href="#">Remove Promotions</a></li>
                    </ul>
                </div>

                <div class="menu-item two-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-user"></span>&nbsp&nbspCustomer</a></h4>
                    <ul class="inactive">
                        <li><a href="#">All Customers</a></li>
                        <li><a href="#">Search Customers</a></li>
                    </ul>
                </div>

                <div class="menu-item two-row" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-transfer"></span>&nbspShipping</a></h4>
                    <ul class="inactive">
                        <li><a href="#">Shipping Region</a></li>
                        <li><a href="#">Add Region</a></li>
                    </ul>
                </div>

                <div class="menu-item" style="width:100%;">
                    <h4><a href="#"><span class="glyphicon glyphicon-cog"></span>&nbsp&nbspSetting</a></h4>
                </div>

        </div>

            <div class="col-md-10 ">
            <div style="margin-top: 35px;"></div>

            <h2 class="headline">Update Product</h2>
            <hr class="break">
                            <form class="form-horizontal" form name="submit_form" id="submit_form" action="/catalog/showdata/" method="post">
                            <input type="hidden" name="id" value="'''+str(product.id)+'''" />
                                <div style="margin-top: 40px;">
                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="ProductID">Product ID</label>
                                        <div class="col-md-3">
                                            <input type="text" name="Pid" value="'''+product.Pid+'''" placeholder="Please enter product ID." style="width: 100%; height: 30px;" />
                                        </div>
                                    </div> 
                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Name">Name</label>
                                            <div class="col-md-5"> 
                                                <input type="text" name="Pname" value="'''+product.Pname+'''" placeholder="Please enter product name." style="width: 100%; height: 30px;" />
                                        </div>
                                    </div> 
                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Brand">Brand</label>
                                        <div class="col-md-5">                                             
                                            <input type="text" name="Pbrand" value="'''+product.Pbrand+'''" placeholder="Please enter product brand." style="width: 100%; height: 30px;" />
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Price">Price </label>
                                        <div class="col-md-3">          
                                            <input type="text" name="Pprice" value="'''+str(product.Pprice)+'''"  placeholder="Please enter product price." style="width: 100%; height: 30px;" />
                                        </div>
                                    </div>


                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Price">Amount </label>
                                        <div class="col-md-3">          
                                            <input type="number" value="'''+str(product.Pamount)+'''" min="0" name="Pamount"/>
                                        </div>
                                    </div>


                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Descript">Description</label>
                                        <div class="col-md-5">
                                            <textarea id="description" rows="10" cols="50" name="Pdetail" value="'''+product.Pdetail+'''" placeholder="Please enter product detail."></textarea>
                                            <style>
                                                .userInput {
                                                text-align: left;
                                                margin: 1px;
                                                padding: 1px;
                                                width: 500px;
                                                height: 300px;
                                                vertical-align: top;
                                                }
                                            </style>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Category">Category</label>
                                        <div class="col-md-3">                                             
                                            <input type="radio" name="Ptype" value="SkinCare" '''+SkinCareSelected+''' /> SkinCare
                                            <br />
                                            <input type="radio" name="Ptype" value="BaseMakeup" '''+BaseMakeupSelected+'''/> Base Makeup
                                            <br />
                                            <input type="radio" name="Ptype" value="PointMakeup" '''+PointMakeupSelected+'''/> Point Makeup
                                            <br />
                                            <input type="radio" name="Ptype" value="Accessories" '''+AccessoriesSelected+'''/> Accessories
                                            <br />
                                            <input type="radio" name="Ptype" value="Fragrance" '''+FragranceSelected+'''/> Fragrance
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label class="control-label col-md-2 text-size-15" for="Image">Product image</label>
                                        <div class="col-md-3">                                                      
                                            <input type="text" name="Ppicture" value="'''+product.Ppicture+'''" placeholder="Please enter link of product picture." style="width: 100%; height: 30px;" />
                                        </div>
                                    </div>
                                    
                                    
                                    <div class="form-group">        
                                        <div class="col-md-offset-2 col-md-8 text-size-15">
                                            <input type="button" value="Cancel" />
                                            <input type="submit" value="Submit" />
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>




              </form>
          </div>




        </div>

    </div>

    </div>
    </div>

</body>
</html>'''

    return HttpResponse (message)

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
    with connection.cursor() as cursor:
         cursor.execute("DELETE FROM product where id= %s", _id)
         
    return HttpResponseRedirect('/catalog/select/')