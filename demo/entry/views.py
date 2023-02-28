# from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def check(request):
    print('entere man')
    # return render('check.html',{'name':'Rohith'})
    template = loader.get_template('check.html')
    context = {
        'name':'Rohith',
        }
    return HttpResponse(template.render(context, request))
