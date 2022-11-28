from django.shortcuts import render

# Create your views here.

def appdistribute(request):
    print("hello")
    return render(request, 'appdistribute.html')

def apphistory(request):
    print("hello")
    return render(request, 'apphistory.html')
