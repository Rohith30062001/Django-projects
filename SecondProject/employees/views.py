from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, user_logged_in
from django.contrib import messages
from datetime import date
from employees.models import Bookings
from django.template import loader
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse('Home')
def login(request):
    return render(request, 'login.html')
    

def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        passw = request.POST['password']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email_id = request.POST['email']
        if User.objects.filter(username=user_name).count()==0:
            user = User.objects.create_superuser(username=user_name, password=passw,first_name=firstname,last_name=lastname, email=email_id)
            user.save()
            print('user saved')
        # save the details to database and redirect to login page
            return render(request, 'login.html')
        else:
            messages.info(request,'Username exists!')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

# @api_view(['GET'])
# def printUser(request):
#     print(request.user)


def loginperson(request):
    usernme = request.POST['username']
    passwrd = request.POST['password']
    user = authenticate( username= usernme, password = passwrd)
    # need to check the data in database to give access
    # return render(request, 'home.html')
    if user is not None:
        template = loader.get_template('home.html')
        context = {
            'userName':usernme,
            }
        login(request)
        print('the current user:', request.user)
        return HttpResponse(template.render(context, request))
        # return redirect('/home')
        # template = loader.get_template('home.html')
        # context = {
        #     'name':usernme,
        #     }
        # return HttpResponse(template.render(context, request))
    else:
        messages.info(request,'No user Found')
        return render(request, 'login.html')
def logout(request):
    return redirect('/loginuser')

def book(request):
    print('booked')
    if request.method == 'POST':
        # username = request.user
        username = request.GET.get('user')
        dest = request.POST['destination']
        if request.POST['date']:
            tripdate = request.POST['date']
        else:
            tripdate = date.today()
        print('****************************',dest, date, username)
        if request.GET.get('price'):
            price = request.GET.get('price')
        else:
            price = 600
        bookDate = date.today()
        book = Bookings(destnation = dest, tripDate = tripdate, bookingDate = bookDate, userName = username, price = price)
        book.save()
        return render(request, 'thankyou.html', {'data':'BOOKING CONFIRMED!'})
    else:
        return HttpResponse('something wrong')

def viewBookings(request):
    username = request.GET.get('user')
    print('&&&&&&&&&&&&&&&&',username)
    data = Bookings.objects.all().values()
    data = data.filter(userName = username)
    print('###############',data)
    template = loader.get_template('bookings.html')
    context = {
        'orderDetails':data,
        }
    return HttpResponse(template.render(context, request))

def cancelbooking(request):
    id = request.GET.get('id')
    print('the data to delte is',id)
    # Bookings.delete(id)
    # x = Bookings.objects.all()[int(id)]
    # x.delete()
    Bookings.objects.filter(id=id).delete()
    return render(request, 'thankyou.html', {'data':'CANCEL CONFIRMED!'})

def packages(request):
    return render(request, 'packages.html')