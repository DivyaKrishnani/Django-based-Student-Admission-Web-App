
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import RegisterUser
from django.template import loader
from django.shortcuts import render, render_to_response, redirect
from django.contrib import messages


def index(request):
	return render(request, 'homepage.html')

"""
def homepage2(request):
	return render(request, 'homepage2.html')
"""
"""
def loginsignup(request):
	return render(request, 'loginsignup.html')
"""

def login_view(request):
    if request.method == "GET":
        return render(request,'login.html')

    elif request.method == "POST":
        username_temp = request.POST.get('email')
        password_temp = request.POST.get('usrpass')
        if(len(RegisterUser.objects.filter(email=username_temp,password=password_temp))!=0):
            userss=RegisterUser.objects.get(email=username_temp)
            #return HttpResponse("<h3>Succesfully Logged In</h3>")
            return redirect('/form/')
        else:
            messages.error(request,'Please Enter Correct Username/Password')
            return redirect('login_view')
           
            #return render(request,"login.html")
            #messages.add_message(request, messages.INFO, 'Hello world.')



def signup(request):
    if request.method == "GET":
        return render(request,'signup.html')

    elif request.method == "POST":
        firstusername_temp = user_obj=request.POST.get('firstusrname')
        lastusername_temp = user_obj=request.POST.get('lastusrname')

        password_temp = request.POST.get('pass')
        phone = request.POST.get('tel')
        email_temp = request.POST.get('email')
        all_user=RegisterUser.objects.all()
        flag=0
        for a in all_user:
            if a.email==email_temp:
                flag=1
        if flag==1:
            return HttpResponse("<h3>Username all ready there.<br>Choose a different username</h3>"
                                "<a href=''><input type='button' value='SignUp'></a>")
        else:
            user_instance = RegisterUser.objects.create(firstname=firstusername_temp,lastname=lastusername_temp,password=password_temp,phone_number=phone,email=email_temp)
            messages.error(request,'Succesfully Signed Up')
            return redirect('signup')
