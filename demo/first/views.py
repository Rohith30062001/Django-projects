# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# def first(request):
#     return HttpResponse("Hello world!")


from django.http import HttpResponse
from django.template import loader
from first.models import First

def first(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def second(request):
    template = loader.get_template('mysecond.html')
    return HttpResponse(template.render())
def readData(request):
    data = First.objects.all().values()
    template = loader.get_template('render.html')
    context = {
      'mymembers': data,
    }
    return HttpResponse(template.render(context, request))
def insert(request):
    first = First(firstname = 'Jayanth', lastname = 'Sandireddy')
    first.save()
    return HttpResponse('Done')