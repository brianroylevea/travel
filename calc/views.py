from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'brian'})
def add(request):
    val1= int(request.GET['num1'])
    val2= int(request.GET['num2'])
    val3 =val1+val2
    return render(request,'result.html',{'val':val3 })


