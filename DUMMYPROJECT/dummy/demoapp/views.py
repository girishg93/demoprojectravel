from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import place
from . models import team

# Create your views here.
def index(request):
    obj=place.objects.all()
    obj1 = team.objects.all()
    return render(request,"index.html",{'result': obj,'result1': obj1})


def aboutus(request):
    return render(request,"aboutus.html")

"""def home(request):
    return render(request,"home.html")
def addition(request):
    x=int(request.GET['txt1'])
    y=int(request.GET['txt2'])
    z=x+y
    sub = x - y
    mul = x * y
    div = x / y

    return render(request,"result.html",{'res':z,'res1':sub,'res2':mul,'res3':div})"""


