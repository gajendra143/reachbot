from django.shortcuts import render, redirect
from pagetwo.forms import RegisterForm
from django.db.transaction import connections
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, userloginform
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def pagetwo(request):
    return render(request,'page2.html')

def Register(request):
    formObj = RegisterForm()

    print(request.GET)

    if request.method == 'POST':
        formObj = RegisterForm(request.POST)

        if formObj.is_valid():
            formObj.save()

            #pass
    # print(formObj)
    return render(request, 'regist.html', {'form': formObj})

def about(request):
    return render(request, 'about1.html')

def services(request):
    return render(request,'service.html')

# def rstar(request):
#     form = UserForm()
#
#     print(request.GET)
#
#     if request.method == 'POST':
#         form= UserForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#     return render(request, 'register.html', {'form': form})

def rstar(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            #messages.success(request, 'Account created successfully')
            return redirect(pagetwo)

    else:
        f = CustomUserCreationForm()

    return render(request, 'register.html', {'form': f})

def team(request):
    return render(request, 'team.html')


def port(request):
    return render(request, 'port.html')

def blog(request):
    return render(request, 'blog.html')



def userLogin(request):
    if request.user.username:
        return redirect(port)

    form = userloginform()
    message = ''
    if request.method == 'POST':
        form = userloginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # print(username)
            password = form.cleaned_data['password']
            # print(password)
            user = authenticate(
                username=username,
                password=password
            )

        if user is None:
                message = 'invalid login details'
        else:
                login(request, user)
                return redirect(pagetwo)
    return render(request, 'login.html', {'form': form, 'msg': message})
#
def userlogout(request):
    logout(request)
    return redirect(pagetwo)


def coder(request):
    return render(request, 'coder.html')


def design(request):
    return render(request, 'design.html')

def wordpress(request):
    return render(request, 'wordpress.html')

def expert(request):
    return render(request, 'expert.html')