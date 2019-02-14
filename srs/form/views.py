from django.http import HttpResponse,Http404
from .models import appform1
from django.template import loader
from django.shortcuts import render, render_to_response, redirect		
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#from django.contrib.auth import login

from django.contrib import messages
def appform(request):
	if request.method == "GET":
		return render(request,'reg2.html')
	elif request.method == "POST":
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		email=request.POST.get('email')
		contact_number=request.POST.get('cno')
		aadhar_number = request.POST.get('ano')
		quo = request.POST.get('quo')
		category = request.POST.get('cat')
		dob = request.POST.get('dob')
		gender = request.POST.get('gen')
		boe = request.POST.get('boe')
		year = request.POST.get('yop')
		result = request.POST.get('res')
		brno = request.POST.get('brno')
		mothna = request.POST.get('mna')
		mothc = request.POST.get('mno')
		motho = request.POST.get('mo')
		fathna = request.POST.get('fna')
		fathc = request.POST.get('fno')
		fatho = request.POST.get('fo')
		ques = request.POST.get('ind')
		add1 = request.POST.get('ad1')
		add2 = request.POST.get('ad2')
		country = request.POST.get('con')
		state = request.POST.get('state')
		city = request.POST.get('city')
		pincode = request.POST.get('pc')
		padd1 = request.POST.get('pad1')
		padd2 = request.POST.get('pad2')
		pcountry = request.POST.get('pcon')
		pstate = request.POST.get('pstate')
		pcity = request.POST.get('pcity')
		ppincode = request.POST.get('ppc')
		bank = request.POST.get('bnk')
		accn = request.POST.get('acch')
		accno = request.POST.get('accno')
		ifs = request.POST.get('ifsc')
		pic =request.POST.get('pic')
		sign = request.POST.get('sign')
		mark = request.POST.get('mark')
		
		form_instance = appform1.objects.create(fname=fname,lname=lname, email=email,contact_number=contact_number,aadhar_number=aadhar_number,quo=quo,category=category,dob=dob,gender=gender,boe=boe,year=year,result=result,mothna=mothna,mothc=mothc,motho=motho,fathna=fathna,fathc=fathc,fatho=fatho, ques= ques, add1=add1,add2=add2,country=country,state=state,city=city,pincode=pincode,padd1=padd1,padd2=padd2,pcountry=pcountry,pstate=pstate,pcity=pcity,ppincode=ppincode,bank=bank,accn=accn,accno=accno,ifs=ifs)
	
		
		#return render(request,'reg2.html',{'forms':form_instance})
		#return HttpResponse("<h3>Successfullty Registered</h3>")
		messages.error(request,'Succesfully Registered')
		return redirect('signup')

