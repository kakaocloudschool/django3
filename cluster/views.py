from django.shortcuts import render

# Create your views here.
def addcluster(request):
    print("hello")
    return render(request, 'addcluster.html')