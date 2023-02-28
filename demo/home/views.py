# from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def login(request):
    print('entered login man', request)
    # if request.method == 'GET':
    #     print('entered get req')
    # # return render('check.html',{'name':'Rohith'})
    #     template = loader.get_template('login.html')
    #     return HttpResponse(template.render())
    if request.method == 'POST':
        print('entered post req')
        username = request.POST['username']
        password = request.POST['password']
        print('yess login receved', username, password)
        return HttpResponse('Done')
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render())
def register(request):
    print('received')
