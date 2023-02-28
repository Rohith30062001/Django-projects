from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "all.html")

def calc(request):
    num1 = request.POST['num1']
    operator = request.POST['operator']
    num2 = request.POST['num2']
    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        if operator == '+':
            res = a + b
        if operator == '-':
            res = a - b
        if operator == '*':
            res = a * b
        if operator == '/':
            res = a / b
        return render(request, "result.html", {"result": res})
    else:
        res = "something wrong happened"
        return render(request, "result.html", {"result": res})

def addition(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a + b

        return render(request, "result.html", {"result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})


def subtraction(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a - b

        return render(request, "result.html", {"result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})


def multiplication(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a * b

        return render(request, "result.html", {"result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})



def division(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    
    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)

        if b == 0:
            res = "Zero divide error"
            return render(request, "result.html", {"result": res})
        else:
            res = a / b
            return render(request, "result.html", {"result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})