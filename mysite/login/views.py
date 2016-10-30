from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.conf import settings
from login.models import logUsers


def index(request):
	page = '''
				<!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Login - TRiANGLE</title>
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
                    <li><a href="../catalog/base_makeup">Base Makeup</a></li>
                    <li><a href='../catalog/point_makeup'>Point Makeup</a></li>
                    <li><a href="../catalog/accessories">Accessories</a></li>
                    <li><a href="../catalog/fragrance">Fragrance</a></li>
                  </ul>
                </li>
                <li><a href="#">CONTACT</a></li>
                <li class="dropdown">
                  <a class="dropdown-toggle" data-toggle="dropdown" href="#"><span class="glyphicon glyphicon-user"></span>&nbsp&nbspMEMBER<span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="/login/"><span class="glyphicon glyphicon-log-in"></span>&nbsp&nbspLog in</a></li>
                    <li><a href="/register/"><span class="glyphicon glyphicon-edit"></span>&nbsp&nbspSign Up</a></li>
                  </ul>
                </li>
                <li><a href="#"><span class="glyphicon glyphicon-shopping-cart"></span></a></li>
              </ul>
            </div>
          </div>
        </nav>
        <br><br>
        <section class="jumbotron" style="background-image: url('/static/img/mainpic/Skincare.jpg');">
          <div class="container">
            <div class="row text-center">
              <h2>TRiANGLE Cosmetic</h2>
              <h3>Makeup Power</h3>
              <!--<a class="btn btn-primary" href="#">See all</a>-->
            </div>
          </div>
        </section>
        <div class="text-center" style="color: #FFDEAD;"><h2>Log In</h2></div>
        <br>
        <form class="form-horizontal" name="submit_form" id="submit_form" action="/login/attempt/" method="post">
         
            <div class="form-group">
              <label class="control-label col-xs-offset-4 col-sm-1" for="username">Username:</label>
              <div class="col-sm-2">
                <input name="user" type="text" class="form-control"  id="user" placeholder="Enter username">
              </div>
            </div>
            <div class="form-group">
              <label class="control-label col-xs-offset-4 col-sm-1" for="pwd">Password:</label>
              <div class="col-sm-2"> 
                <input name="pwd" type="password" class="form-control"  id="pwd" placeholder="Enter password">
              </div>
            </div>
            <div class="form-group"> 
              <div class="col-sm-offset-5 col-sm-10">
                <div class="checkbox">
                  <label><input type="checkbox" name="remember_me"> Remember me</label>
                </div>
              </div>
            </div>
            <div class="form-group"> 
              <div class="col-sm-offset-5 col-sm-10">
                <button type="submit" class="btn btn-primary" value="SignIn">Sign In</button>
                <a href="/register?" button type="button" class="btn btn-default" value="Create">Create Account</a></button>
              </div>
            </div>
          
        </form>             
      </body>
    </html>
		'''
	return HttpResponse(page)

@csrf_exempt
def attempt(request):

	if request.method == "POST":
		useratt = request.POST.get("user", ".")
		passatt = request.POST.get("pwd", ".")
		if not request.POST.get('remember_me', None):
			request.session.set_expiry(0)
		print(useratt)
		print(passatt)


	try:
		user = logUsers.objects.get(username = useratt)
		print(user.username)
		print(user.password)
		if user.password == passatt:
			return HttpResponseRedirect('/home/') # succress login 
		else:
			return HttpResponseRedirect('/login/failattempt/') 
	except:
		return HttpResponseRedirect('/login/failattempt/') 

	

	


def failattempt(request):
	page = '''	
				<!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Login - TRiANGLE</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
      <link href='https://fonts.googleapis.com/css?family=Roboto:300,400,700' rel='stylesheet' type='text/css'>
      <link rel="stylesheet" type="text/css" href="/static/css/codebcatalog.css">
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
                    <li><a href="../catalog/base_makeup">Base Makeup</a></li>
                    <li><a href='../catalog/point_makeup'>Point Makeup</a></li>
                    <li><a href="../catalog/accessories">Accessories</a></li>
                    <li><a href="../catalog/fragrance">Fragrance</a></li>
                  </ul>
                </li>
                <li><a href="#">CONTACT</a></li>
                <li class="dropdown">
                  <a class="dropdown-toggle" data-toggle="dropdown" href="#"><span class="glyphicon glyphicon-user"></span>&nbsp&nbspMEMBER<span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="/login/"><span class="glyphicon glyphicon-log-in"></span>&nbsp&nbspLog in</a></li>
                    <li><a href="/register/"><span class="glyphicon glyphicon-edit"></span>&nbsp&nbspSign Up</a></li>
                  </ul>
                </li>
                <li><a href="#"><span class="glyphicon glyphicon-shopping-cart"></span></a></li>
              </ul>
            </div>
          </div>
        </nav>
        <br><br>
        <section class="jumbotron" style="background-image: url('/static/img/mainpic/Skincare.jpg');">
          <div class="container">
            <div class="row text-center">
              <h2>TRiANGLE Cosmetic</h2>
              <h3>Makeup Power</h3>
              <!--<a class="btn btn-primary" href="#">See all</a>-->
            </div>
          </div>
        </section>
        <div class="text-center" style="color: #FFDEAD;"><h2>Log In</h2></div>
        <br>
				        <div class="container">
				        <div class="alert alert-danger">
				  			<strong>Username or password incorrect.</strong> Please try again.
						</div>  
				        <form class="form-horizontal" name="submit_form" id="submit_form" action="/login/attempt/" method="post">
				            <div class="form-group has-error has-feedback">
							  <label class="control-label col-sm-1" for="usernameError">Username:</label>
							  <div class="col-sm-2">
							    <input type="text" name="user" class="form-control" id="username" placeholder="Enter username">

							  </div>
							</div>
							<div class="form-group has-error has-feedback">
							  <label class="control-label col-sm-1" for="pwd">Password:</label>
							  <div class="col-sm-2"> 
							    <input type="password" name="pwd" class="form-control" id="pwd" placeholder="Enter password">
							  </div>
							  </div>
				          <div class="form-group"> 
				            <div class="col-sm-offset-1 col-sm-10">
				              <div class="checkbox">
				                <label><input type="checkbox" name="remember_me"> Remember me</label>
				              </div>
				            </div>
				          </div>
				          <div class="form-group"> 
				            <div class="col-sm-offset-1 col-sm-10">
				              <button type="submit" class="btn btn-primary" value="SignIn">Sign In</button>
				             <a href="/register?" button type="button" class="btn btn-default" value="Create">Create Account</a></button>
				            </div>
				          </div>
				</form>
				</body>
			    </html>
		'''
	return HttpResponse(page)