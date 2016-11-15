from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.contrib.auth.models import User
from models import CartItem

def index(request): 
  userin=request.user.username
  
  print (userin)
  item = CartItem.objects.filter(username=userin)
  if userin != "":
    userbar = '''<a class="dropdown-toggle" data-toggle="dropdown" href="#"><span class="glyphicon glyphicon-user"></span>&nbsp&nbsp'''+userin+'''<span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="/Profile/"><span class="glyphicon glyphicon-edit"></span>&nbsp&nbspProfile</a></li>
                    <li><a href="/login/"><span class="glyphicon glyphicon-log-in"></span>&nbsp&nbspLog Out</a></li>
                  </ul>'''

  else:
    userbar = '''<a class="dropdown-toggle" data-toggle="dropdown" href="#"><span class="glyphicon glyphicon-user"></span>&nbsp&nbspMEMBER<span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="/login/"><span class="glyphicon glyphicon-log-in"></span>&nbsp&nbspLog In</a></li>
                    <li><a href="/register/"><span class="glyphicon glyphicon-edit"></span>&nbsp&nbspSign Up</a></li>
                  </ul>'''

  page = '''	
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Cart - TRiANGLE</title>
  <meta charset="utf-8" />
  <link href='https://fonts.googleapis.com/css?family=Roboto:300,400,700' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" type="text/css" href="/static/css/codebcatalog.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
           .navbar {
          padding-top: 5px;
          padding-bottom: 5px;
          border: 0;
          border-radius: 0;
          margin-bottom: 0;
          font-size: 18px;
          letter-spacing: 3px;            
        }
        .navbar-nav li a:hover {
          color: #FFDEAD !important;
        }
        .navbar-brand{
          font-size:24px;
          color: #FFDEAD !important;
        }
          </style>
</head>

<body style="background-color:black;color:white">
          <nav class="navbar navbar-inverse navbar-fixed-top">
          <div class="container-fluid">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="/home/" >TRiANGLE</a>
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
              <ul class="nav navbar-nav navbar-right">
                <li><a href="/home/">HOME</a></li>
                <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="/catalog/">CATALOG<span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="../catalog">All</a></li>
                    <li><a href="../catalog/skincare">Skincare</a></li>
                    <li><a href="../catalog/base makeup">Base Makeup</a></li>
                    <li><a href='../catalog/point makeup'>Point Makeup</a></li>
                    <li><a href="../catalog/accessories">Accessories</a></li>
                    <li><a href="../catalog/fragrance">Fragrance</a></li>
                  </ul>
                </li>
                <li><a href="#">CONTACT</a></li>
                <li class="dropdown">
                  '''+userbar+'''
                </li>
                <li><a href="#"><span class="glyphicon glyphicon-shopping-cart"></span></a></li>
              </ul>
            </div>
          </div>
        </nav>
<br><br>
<section class="jumbotron" style="background-image: url('/static/img/mainpic/Loreal.jpg');">
          <div class="container">
            <div class="row text-center">
              <h2>TRiANGLE Cosmetic</h2>
              <h3>Makeup Power</h3>
              <!--<a class="btn btn-primary" href="#">See all</a>-->
            </div>
          </div>
        </section>
        <div class="text-center" style="color: #FFDEAD;"><h2>Cart</h2></div>
        <br>
 </div>
<section class="container">
    <div class="row" style="color: orange;" >
    <div class="row-xs-height">
	'''
  for obj in item :
    page += '''
      	<div class="col-xs-4 col-height" style="height: 600px;">
        	<p style="height: 160px;">
            <span style="color: white">ProductID : </span> '''
    page += obj.Pid
    page += '''<br/>
				<span style="color: white">Product : </span> '''
    page += obj.Pname
    page += '''<br/>
					     <span style="color: white">Price : </span> '''
    page += obj.Pprice
    page += '''<span style="color: white"> THB</span><br/>
        		</p>
				    <img src="/static/img/Photo_Product/'''
    page += obj.Ppicture
    page += '''" />
      		</div> '''
    page += '''</div>
    </div>
    </div>-->
  </section>
</body>
</html>

		'''


  return HttpResponse(page)
