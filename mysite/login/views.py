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
				  <title>:: Sign In ::</title>
				  <meta charset="utf-8">
				  <meta name="viewport" content="width=device-width, initial-scale=1">
				  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
				  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
				  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
				</head>
				<body>

				<div class="container">
				  <h2>:: Sign In ::</h2>

				<form class="form-horizontal" name="submit_form" id="submit_form" action="/login/attempt/" method="post">
				  <div class="form-group">
				    <label class="control-label col-sm-1" for="username">Username:</label>
				    <div class="col-sm-2">
				      <input name="user" type="text" class="form-control"  id="user" placeholder="Enter username">
				    </div>
				  </div>
				  <div class="form-group">
				    <label class="control-label col-sm-1" for="pwd">Password:</label>
				    <div class="col-sm-2"> 
				      <input name="pwd" type="password" class="form-control"  id="pwd" placeholder="Enter password">
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
				      <button type="submit" class="btn btn-success" value="SignIn">Sign In</button>
				      <button type="button" class="btn btn-default" value="Create"><a href="/register?">Create Account</a></button>
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
			return HttpResponseRedirect('/login/') # succress login 
		else:
			return HttpResponseRedirect('/login/failattempt/') 
	except:
		return HttpResponseRedirect('/login/failattempt/') 

	

	


def failattempt(request):
	page = '''	
				<!DOCTYPE html>
				<html lang="en">
				<head>
				  <title>:: Sign In ::</title>
				  <meta charset="utf-8">
				  <meta name="viewport" content="width=device-width, initial-scale=1">
				  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
				  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
				  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
				</head>
				<body>

				<div class="container">
				  <h2>:: Sign In ::</h2>
				<div class="alert alert-danger">
  				  <strong>Username or password incorrect.</strong> Please try again.
				</div>
				<form class="form-horizontal" name="submit_form" id="submit_form" action="/login/attempt/" method="post">
				  <div class="form-group">
				    <label class="control-label col-sm-1" for="username">Username:</label>
				    <div class="col-sm-2">
				      <input type="text" class="form-control" name="user" id="user" placeholder="Enter username">
				    </div>
				  </div>
				  <div class="form-group">
				    <label class="control-label col-sm-1" for="pwd">Password:</label>
				    <div class="col-sm-2"> 
				      <input type="password" class="form-control" name="pwd" id="pwd" placeholder="Enter password">
				    </div>
				  </div>
				  <div class="form-group"> 
				    <div class="col-sm-offset-1 col-sm-10">
				      <div class="checkbox">
				        <label><input type="checkbox"> Remember me</label>
				      </div>
				    </div>
				  </div>
				  <div class="form-group"> 
				    <div class="col-sm-offset-1 col-sm-10">
				      <button type="submit" class="btn btn-success" value="SignIn">Sign In</button>
				      <button type="button" class="btn btn-default" value="Create"><a href="/register?">Create Account</a></button>
				    </div>
				  </div>
				</form>
				</body>
				</html>
		'''
	return HttpResponse(page)