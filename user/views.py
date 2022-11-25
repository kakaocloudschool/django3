from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def logout(request):
    print("")
    auth_logout(request)
    print("hello my name is chi")
    return redirect('/user/login')

def changepw(request):
    return render(request, 'changepw.html')

def login(request):
    if request.method=="GET":
        loginForm = AuthenticationForm()
        context = {'loginForm':loginForm}
        return render(request, 'login.html', context)
    elif request.method=="POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
        return redirect('/board/list')

# Create your views here.
def signup(request):
    if request.method=="GET":
        signupForm = UserCreationForm()
        context = {'signupForm':signupForm}
        return render(request, 'user/signup.html', context)

    elif request.method=="POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            user.save()
        return redirect('/board/list')
