from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from register.models import UserData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
  userin=request.user.username
  print (userin)
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
    <title>Sign Up - TRiANGLE</title>
    <meta charset="utf-8" />

    <link href="https://fonts.googleapis.com/css?family=Cabin+Condensed|PT+Sans+Caption|Viga" rel="stylesheet">

    <link href='https://fonts.googleapis.com/css?family=Roboto:300,400,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="/static/css/codebcatalog.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <link type="text/css" rel="stylesheet" href="/static/css/style_beboonn.css">

</head>

<body>

    <body>

        <nav class="navbar navbar-inverse navbar-fixed-top navfont">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="/home/">TRiANGLE
        <!--<img style="max-width:100px; margin-top: -7px;"
             src="../static/img/logo2.png"/>--></a>
                </div>
                <div class="collapse navbar-collapse" id="myNavbar">
                    <ul class="nav navbar-nav navbar-right">
                        <!--                    <li><a href="/home/">HOME</a></li>-->
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
                        <li><a href="#"><span class="glyphicon glyphicon-shopping-cart"></span></a></li>
                        <li class="dropdown">
                            <a class="dropdown-toggle" data-toggle="dropdown" href="#"><span class="glyphicon glyphicon-user"></span>&nbsp&nbspMEMBER
          <span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="/login/"><span class="glyphicon glyphicon-log-in"></span>&nbsp&nbspLog in</a></li>
                                <li><a href="/register/"><span class="glyphicon glyphicon-edit"></span>&nbsp&nbspSign Up</a></li>
                            </ul>
                        </li>
                    </ul>
                    <form class="navbar-form navbar-right hover-summit-botton">
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Search">
                        </div>
                        <button type="submit" class="btn btn-default btn-summit"><span class="glyphicon glyphicon-search"></span></button>
                    </form>
                </div>
            </div>
        </nav>
        <!--navbar-->

        <div id="myCarousel" class="carousel slide" data-ride="carouselx">

            <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
            <li data-target="#myCarousel" data-slide-to="1"></li>

            <div class="carousel-inner" role="listbox">




                <section class="jumbotron item active" style="background-image: url('/static/img/mainpic/box_1.png');">
                    <div class="container">
                        <div class="row text-center">
                            <div class="triangle-white-box1 col-s12">
                                <span class="triangle-header-text1">
          TRiANGLE Cosmetic
        </span>
                                <br />
                                <span class="under-triangle-header">
          Makeup Power
        </span>
                            </div>
                        </div>
                    </div>
                </section>

                <section class="jumbotron item" style="background-image: url('/static/img/mainpic/box_3.png');">
                    <div class="container">
                        <div class="row text-center">
                            <div class="triangle-white-box2 col-s12">
                                <!--
                            <span class="triangle-header-text2">
          Money can't buy happiness
        </span>
<br>
<span class="triangle-header-text2">
                               But It can buy Makeup!
                           </span>
-->
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>

        </div>

        <!--    ----triangle header------>

        <div class="text-center login login-box">
            <h2>Sign Up</h2>
        </div>
        <br>
        <div class="container">
            <form class="form-horizontal login-form" method="post" name="submit_form" id="submit_form" action="/register/attempt/">

                <div class="form-group">
                    <label class="control-label col-xs-2" for="firstName">First Name:</label>
                    <div class="col-xs-2">
                        <input type="text" class="form-control" name="firstName" id="firstName" placeholder="First Name">
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="lastName">Last Name:</label>
                    <div class="col-xs-2">
                        <input type="text" class="form-control" name="lastName" id="lastName" placeholder="Last Name">
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="username">Username:</label>
                    <div class="col-xs-2">
                        <input type="text" class="form-control" name="username" id="username" placeholder="Username" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="pwd">Password:</label>
                    <div class="col-xs-2">
                        <input type="password" class="form-control" name="pwd" id="pwd" maxlength="8" placeholder="6-8 characters" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="pwd2">Verify Password:</label>
                    <div class="col-xs-2">
                        <input type="password" class="form-control" name="pwd2" id="pwd2" maxlength="8" placeholder="type again" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="email">Email Address:</label>
                    <div class="col-xs-3">
                        <input type="email" class="form-control" name="email" id="email" placeholder="ex. example@triangle.com" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="email">Verify Email Address:</label>
                    <div class="col-xs-3">
                        <input type="email" class="form-control" name="email2" id="email2" placeholder="ex. example@triangle.com" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="gender">Gender:</label>
                    <div class="col-xs-3">
                        <div class="radio">
                            <label>
                                <input type="radio" name="gender" value="m" checked>Male</label>
                        </div>
                        <div class="radio">
                            <label>
                                <input type="radio" name="gender" value="f">Female</label>
                        </div>
                        <div class="radio">
                            <label>
                                <input type="radio" name="gender" value="o">Other</label>
                        </div>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="dateBD">Date of Birth:</label>
                    <div class="form-inline">
                        &nbsp&nbsp
                        <select class="form-control" name="dayBD" id="dayBD">
                            <option value="">Day</option>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                            <option value="6">6</option>
                            <option value="7">7</option>
                            <option value="8">8</option>
                            <option value="9">9</option>
                            <option value="10">10</option>
                            <option value="11">11</option>
                            <option value="12">12</option>
                            <option value="13">13</option>
                            <option value="14">14</option>
                            <option value="15">15</option>
                            <option value="16">16</option>
                            <option value="17">17</option>
                            <option value="18">18</option>
                            <option value="19">19</option>
                            <option value="20">20</option>
                            <option value="21">21</option>
                            <option value="22">22</option>
                            <option value="23">23</option>
                            <option value="24">24</option>
                            <option value="25">25</option>
                            <option value="26">26</option>
                            <option value="27">27</option>
                            <option value="28">28</option>
                            <option value="29">29</option>
                            <option value="30">30</option>
                            <option value="31">31</option>
                        </select>
                        <select class="form-control" name="monthBD" id="monthBD">
                            <option value="">Month</option>
                            <option value="1">January</option>
                            <option value="2">Febuary</option>
                            <option value="3">March</option>
                            <option value="4">April</option>
                            <option value="5">May</option>
                            <option value="6">June</option>
                            <option value="7">July</option>
                            <option value="8">August</option>
                            <option value="9">September</option>
                            <option value="10">October</option>
                            <option value="11">November</option>
                            <option value="12">December</option>
                        </select>
                        <select class="form-control" name="yearBD" id="yearBD">
                            <option value="">Year</option>
                            <option value="1916">1916</option>
                            <option value="1917">1917</option>
                            <option value="1918">1918</option>
                            <option value="1919">1919</option>
                            <option value="1920">1920</option>
                            <option value="1921">1921</option>
                            <option value="1922">1922</option>
                            <option value="1923">1923</option>
                            <option value="1924">1924</option>
                            <option value="1925">1925</option>
                            <option value="1926">1926</option>
                            <option value="1927">1927</option>
                            <option value="1928">1928</option>
                            <option value="1929">1929</option>
                            <option value="1930">1930</option>
                            <option value="1931">1931</option>
                            <option value="1932">1932</option>
                            <option value="1933">1933</option>
                            <option value="1934">1934</option>
                            <option value="1935">1935</option>
                            <option value="1936">1936</option>
                            <option value="1937">1937</option>
                            <option value="1938">1938</option>
                            <option value="1939">1939</option>
                            <option value="1940">1940</option>
                            <option value="1941">1941</option>
                            <option value="1942">1942</option>
                            <option value="1943">1943</option>
                            <option value="1944">1944</option>
                            <option value="1945">1945</option>
                            <option value="1946">1946</option>
                            <option value="1947">1947</option>
                            <option value="1948">1948</option>
                            <option value="1949">1949</option>
                            <option value="1950">1950</option>
                            <option value="1951">1951</option>
                            <option value="1952">1952</option>
                            <option value="1953">1953</option>
                            <option value="1954">1954</option>
                            <option value="1955">1955</option>
                            <option value="1956">1956</option>
                            <option value="1957">1957</option>
                            <option value="1958">1958</option>
                            <option value="1959">1959</option>
                            <option value="1960">1960</option>
                            <option value="1961">1961</option>
                            <option value="1962">1962</option>
                            <option value="1963">1963</option>
                            <option value="1964">1964</option>
                            <option value="1965">1965</option>
                            <option value="1966">1966</option>
                            <option value="1967">1967</option>
                            <option value="1968">1968</option>
                            <option value="1969">1969</option>
                            <option value="1970">1970</option>
                            <option value="1971">1971</option>
                            <option value="1972">1972</option>
                            <option value="1973">1973</option>
                            <option value="1974">1974</option>
                            <option value="1975">1975</option>
                            <option value="1976">1976</option>
                            <option value="1977">1977</option>
                            <option value="1978">1978</option>
                            <option value="1979">1979</option>
                            <option value="1980">1980</option>
                            <option value="1981">1981</option>
                            <option value="1982">1982</option>
                            <option value="1983">1983</option>
                            <option value="1984">1984</option>
                            <option value="1985">1985</option>
                            <option value="1986">1986</option>
                            <option value="1987">1987</option>
                            <option value="1988">1988</option>
                            <option value="1989">1989</option>
                            <option value="1990">1990</option>
                            <option value="1991">1991</option>
                            <option value="1992">1992</option>
                            <option value="1993">1993</option>
                            <option value="1994">1994</option>
                            <option value="1995">1995</option>
                            <option value="1996">1996</option>
                            <option value="1997">1997</option>
                            <option value="1998">1998</option>
                            <option value="1999">1999</option>
                            <option value="2000">2000</option>
                            <option value="2001">2001</option>
                            <option value="2002">2002</option>
                            <option value="2003">2003</option>
                            <option value="2004">2004</option>
                            <option value="2005">2005</option>
                            <option value="2006">2006</option>
                            <option value="2007">2007</option>
                            <option value="2008">2008</option>
                            <option value="2009">2009</option>
                            <option value="2010">2010</option>
                            <option value="2011">2011</option>
                            <option value="2012">2012</option>
                            <option value="2013">2013</option>
                            <option value="2014">2014</option>
                            <option value="2015">2015</option>
                            <option value="2016">2016</option>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="phone">Phone Number:</label>
                    <div class="col-xs-2">
                        <input type="text" class="form-control" name="phone" id="phone" placeholder="0xx-xxx-xxxx">
                    </div>
                </div>

                <div class="form-group">
                    <div class="col-sm-offset-2 col-sm-10">
                        <button type="submit" class="btn btn-signin" value="Submit">Sign Up</button>
                        <a href="/login?" button type="button" class="btn btn-default btn-create" value="Cancel">Cancel</a>
                    </div>
                </div>



            </form>
        </div>

        <footer class="text-center">
            <!--
        <a class="up-arrow" href="/home" data-toggle="tooltip" title="TO TOP">
            <span class="glyphicon glyphicon-chevron-up"></span>
        </a>
-->
            <div class="col-sm-6">
                <a href="#">ABOUT US</a>
                <br>
                <span>...............</span>
                <br>
                <span>..............</span>
                <br>
                <span>..............</span>
            </div>
            <div class="col-sm-6">
                <span>Contact Us</span>
            </div>
        </footer>

        <script>
            $(document).ready(function () {
                        // Initialize Tooltip
                        $('[data-toggle="tooltip"]').tooltip();
        </script>

    </body>

</html>
		'''


  return HttpResponse(page)


@csrf_exempt
def attempt (request):
    if request.method == "POST":
        firstname = request.POST.get("firstName", "")
        lastname = request.POST.get("lastName", "")
        username = request.POST.get("username", "")
        password = request.POST.get("pwd", "")
        password2 = request.POST.get("pwd2", "")
        email = request.POST.get("email","")
        email2 = request.POST.get("email2","")
        gender = request.POST.get("gender", "")
        phonenum = request.POST.get("phone", "")
        dateBD = request.POST.get("dateBD", "")
        monthBD = request.POST.get("monthBD", "")
        yearBD = request.POST.get("yearBD", "")

        dateofbirth = dateBD +"/"+ monthBD +"/"+ yearBD

        print firstname
        print lastname
        print username
        print email
        print gender
        print dateofbirth
        print phonenum

        if(password!=password2):
        	return HttpResponseRedirect('/register/failattempt/?id=pass')

        if(email!=email2):
        	return HttpResponseRedirect('/register/failattempt/?id=email')

        try:
        	user = User.objects.get(username = username)
        	return HttpResponseRedirect('/register/failattempt/?id=user')
        except :
        	print ""


        try:
        	user = User.objects.get(email = email)
        	return HttpResponseRedirect('/register/failattempt/?id=email2')
        except :
        	print ""

        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        with connection.cursor() as cursor:
           	cursor.execute("INSERT INTO userdata (username, gender, dateofbirth, phonenum) VALUES (%s, %s, %s, %s)", (username, gender, dateofbirth, phonenum))

        login(request, user)
    return HttpResponseRedirect('/home/')


def failattempt (request):

  userin=request.user.username
  print (userin)
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



  _id = request.GET.get('id','')
  msg = ""

  if _id == 'pass':
    msg = "Both password must be the same"
  elif _id == 'email':
    msg = "Both email must be the same"
  elif _id == 'user':
    msg = "Username already in use"
  elif _id == 'email2':
    msg = "Email already in use"

  page = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Sign Up - TRiANGLE</title>
    <meta charset="utf-8" />

    <link href="https://fonts.googleapis.com/css?family=Cabin+Condensed|PT+Sans+Caption|Viga" rel="stylesheet">

    <link href='https://fonts.googleapis.com/css?family=Roboto:300,400,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="/static/css/codebcatalog.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <link type="text/css" rel="stylesheet" href="/static/css/style_beboonn.css">

</head>

<body>

    <body>

        <nav class="navbar navbar-inverse navbar-fixed-top navfont">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="/home/">TRiANGLE
        <!--<img style="max-width:100px; margin-top: -7px;"
             src="../static/img/logo2.png"/>--></a>
                </div>
                <div class="collapse navbar-collapse" id="myNavbar">
                    <ul class="nav navbar-nav navbar-right">
                        <!--                    <li><a href="/home/">HOME</a></li>-->
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
                        <li><a href="#"><span class="glyphicon glyphicon-shopping-cart"></span></a></li>
                        <li class="dropdown">
                            <a class="dropdown-toggle" data-toggle="dropdown" href="#"><span class="glyphicon glyphicon-user"></span>&nbsp&nbspMEMBER
          <span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="/login/"><span class="glyphicon glyphicon-log-in"></span>&nbsp&nbspLog in</a></li>
                                <li><a href="/register/"><span class="glyphicon glyphicon-edit"></span>&nbsp&nbspSign Up</a></li>
                            </ul>
                        </li>
                    </ul>
                    <form class="navbar-form navbar-right hover-summit-botton">
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Search">
                        </div>
                        <button type="submit" class="btn btn-default btn-summit"><span class="glyphicon glyphicon-search"></span></button>
                    </form>
                </div>
            </div>
        </nav>
        <!--navbar-->

        <div id="myCarousel" class="carousel slide" data-ride="carouselx">

            <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
            <li data-target="#myCarousel" data-slide-to="1"></li>

            <div class="carousel-inner" role="listbox">




                <section class="jumbotron item active" style="background-image: url('/static/img/mainpic/box_1.png');">
                    <div class="container">
                        <div class="row text-center">
                            <div class="triangle-white-box1 col-s12">
                                <span class="triangle-header-text1">
          TRiANGLE Cosmetic
        </span>
                                <br />
                                <span class="under-triangle-header">
          Makeup Power
        </span>
                            </div>
                        </div>
                    </div>
                </section>

                <section class="jumbotron item" style="background-image: url('/static/img/mainpic/box_3.png');">
                    <div class="container">
                        <div class="row text-center">
                            <div class="triangle-white-box2 col-s12">
                                <!--
                            <span class="triangle-header-text2">
          Money can't buy happiness
        </span>
<br>
<span class="triangle-header-text2">
                               But It can buy Makeup!
                           </span>
-->
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>

        </div>

        <!--    ----triangle header------>

        <div class="text-center login login-box">
            <h2>Sign Up</h2>
        </div>
        <br>
        <div class="container">
            <form class="form-horizontal login-form" method="post" name="submit_form" id="submit_form" action="/register/attempt/">


                <!--               ------------>

                <div class="alert error-box">
                    <strong class="msg">'''+msg+'''</strong> Please try again.
                    <a class="toggle-alert" href="#">Toggle</a>
                </div>


                <!--                ----------->

                <div class="form-group">
                    <label class="control-label col-xs-2" for="firstName">First Name:</label>
                    <div class="col-xs-2">
                        <input type="text" class="form-control" name="firstName" id="firstName" placeholder="First Name">
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="lastName">Last Name:</label>
                    <div class="col-xs-2">
                        <input type="text" class="form-control" name="lastName" id="lastName" placeholder="Last Name">
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="username">Username:</label>
                    <div class="col-xs-2">
                        <input type="text" class="form-control" name="username" id="username" placeholder="Username" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="pwd">Password:</label>
                    <div class="col-xs-2">
                        <input type="password" class="form-control" name="pwd" id="pwd" maxlength="8" placeholder="6-8 characters" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="pwd2">Verify Password:</label>
                    <div class="col-xs-2">
                        <input type="password" class="form-control" name="pwd2" id="pwd2" maxlength="8" placeholder="type again" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="email">Email Address:</label>
                    <div class="col-xs-3">
                        <input type="email" class="form-control" name="email" id="email" placeholder="ex. example@triangle.com" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="email">Verify Email Address:</label>
                    <div class="col-xs-3">
                        <input type="email" class="form-control" name="email2" id="email2" placeholder="ex. example@triangle.com" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="gender">Gender:</label>
                    <div class="col-xs-3">
                        <div class="radio">
                            <label>
                                <input type="radio" name="gender" value="m" checked>Male</label>
                        </div>
                        <div class="radio">
                            <label>
                                <input type="radio" name="gender" value="f">Female</label>
                        </div>
                        <div class="radio">
                            <label>
                                <input type="radio" name="gender" value="o">Other</label>
                        </div>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="dateBD">Date of Birth:</label>
                    <div class="form-inline">
                        &nbsp&nbsp
                        <select class="form-control" name="dayBD" id="dayBD">
                            <option value="">Day</option>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                            <option value="6">6</option>
                            <option value="7">7</option>
                            <option value="8">8</option>
                            <option value="9">9</option>
                            <option value="10">10</option>
                            <option value="11">11</option>
                            <option value="12">12</option>
                            <option value="13">13</option>
                            <option value="14">14</option>
                            <option value="15">15</option>
                            <option value="16">16</option>
                            <option value="17">17</option>
                            <option value="18">18</option>
                            <option value="19">19</option>
                            <option value="20">20</option>
                            <option value="21">21</option>
                            <option value="22">22</option>
                            <option value="23">23</option>
                            <option value="24">24</option>
                            <option value="25">25</option>
                            <option value="26">26</option>
                            <option value="27">27</option>
                            <option value="28">28</option>
                            <option value="29">29</option>
                            <option value="30">30</option>
                            <option value="31">31</option>
                        </select>
                        <select class="form-control" name="monthBD" id="monthBD">
                            <option value="">Month</option>
                            <option value="1">January</option>
                            <option value="2">Febuary</option>
                            <option value="3">March</option>
                            <option value="4">April</option>
                            <option value="5">May</option>
                            <option value="6">June</option>
                            <option value="7">July</option>
                            <option value="8">August</option>
                            <option value="9">September</option>
                            <option value="10">October</option>
                            <option value="11">November</option>
                            <option value="12">December</option>
                        </select>
                        <select class="form-control" name="yearBD" id="yearBD">
                            <option value="">Year</option>
                            <option value="1916">1916</option>
                            <option value="1917">1917</option>
                            <option value="1918">1918</option>
                            <option value="1919">1919</option>
                            <option value="1920">1920</option>
                            <option value="1921">1921</option>
                            <option value="1922">1922</option>
                            <option value="1923">1923</option>
                            <option value="1924">1924</option>
                            <option value="1925">1925</option>
                            <option value="1926">1926</option>
                            <option value="1927">1927</option>
                            <option value="1928">1928</option>
                            <option value="1929">1929</option>
                            <option value="1930">1930</option>
                            <option value="1931">1931</option>
                            <option value="1932">1932</option>
                            <option value="1933">1933</option>
                            <option value="1934">1934</option>
                            <option value="1935">1935</option>
                            <option value="1936">1936</option>
                            <option value="1937">1937</option>
                            <option value="1938">1938</option>
                            <option value="1939">1939</option>
                            <option value="1940">1940</option>
                            <option value="1941">1941</option>
                            <option value="1942">1942</option>
                            <option value="1943">1943</option>
                            <option value="1944">1944</option>
                            <option value="1945">1945</option>
                            <option value="1946">1946</option>
                            <option value="1947">1947</option>
                            <option value="1948">1948</option>
                            <option value="1949">1949</option>
                            <option value="1950">1950</option>
                            <option value="1951">1951</option>
                            <option value="1952">1952</option>
                            <option value="1953">1953</option>
                            <option value="1954">1954</option>
                            <option value="1955">1955</option>
                            <option value="1956">1956</option>
                            <option value="1957">1957</option>
                            <option value="1958">1958</option>
                            <option value="1959">1959</option>
                            <option value="1960">1960</option>
                            <option value="1961">1961</option>
                            <option value="1962">1962</option>
                            <option value="1963">1963</option>
                            <option value="1964">1964</option>
                            <option value="1965">1965</option>
                            <option value="1966">1966</option>
                            <option value="1967">1967</option>
                            <option value="1968">1968</option>
                            <option value="1969">1969</option>
                            <option value="1970">1970</option>
                            <option value="1971">1971</option>
                            <option value="1972">1972</option>
                            <option value="1973">1973</option>
                            <option value="1974">1974</option>
                            <option value="1975">1975</option>
                            <option value="1976">1976</option>
                            <option value="1977">1977</option>
                            <option value="1978">1978</option>
                            <option value="1979">1979</option>
                            <option value="1980">1980</option>
                            <option value="1981">1981</option>
                            <option value="1982">1982</option>
                            <option value="1983">1983</option>
                            <option value="1984">1984</option>
                            <option value="1985">1985</option>
                            <option value="1986">1986</option>
                            <option value="1987">1987</option>
                            <option value="1988">1988</option>
                            <option value="1989">1989</option>
                            <option value="1990">1990</option>
                            <option value="1991">1991</option>
                            <option value="1992">1992</option>
                            <option value="1993">1993</option>
                            <option value="1994">1994</option>
                            <option value="1995">1995</option>
                            <option value="1996">1996</option>
                            <option value="1997">1997</option>
                            <option value="1998">1998</option>
                            <option value="1999">1999</option>
                            <option value="2000">2000</option>
                            <option value="2001">2001</option>
                            <option value="2002">2002</option>
                            <option value="2003">2003</option>
                            <option value="2004">2004</option>
                            <option value="2005">2005</option>
                            <option value="2006">2006</option>
                            <option value="2007">2007</option>
                            <option value="2008">2008</option>
                            <option value="2009">2009</option>
                            <option value="2010">2010</option>
                            <option value="2011">2011</option>
                            <option value="2012">2012</option>
                            <option value="2013">2013</option>
                            <option value="2014">2014</option>
                            <option value="2015">2015</option>
                            <option value="2016">2016</option>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label class="control-label col-xs-2" for="phone">Phone Number:</label>
                    <div class="col-xs-2">
                        <input type="text" class="form-control" name="phone" id="phone" placeholder="0xx-xxx-xxxx">
                    </div>
                </div>

                <div class="form-group">
                    <div class="col-sm-offset-2 col-sm-10">
                        <button type="submit" class="btn btn-signin" value="Submit">Sign Up</button>
                        <a href="/login?" button type="button" class="btn btn-default btn-create" value="Cancel">Cancel</a>
                    </div>
                </div>



            </form>
        </div>

        <footer class="text-center">
            <!--
        <a class="up-arrow" href="/home" data-toggle="tooltip" title="TO TOP">
            <span class="glyphicon glyphicon-chevron-up"></span>
        </a>
-->
            <div class="col-sm-6">
                <a href="#">ABOUT US</a>
                <br>
                <span>...............</span>
                <br>
                <span>..............</span>
                <br>
                <span>..............</span>
            </div>
            <div class="col-sm-6">
                <span>Contact Us</span>
            </div>
        </footer>

        <script>
            $(document).ready(function () {
                        // Initialize Tooltip
                        $('[data-toggle="tooltip"]').tooltip();
        </script>

    </body>

</html>
		'''


  return HttpResponse(page)
