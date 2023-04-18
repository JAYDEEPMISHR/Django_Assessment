from django.shortcuts import render
from .models import User

# Create your views here.

def index(request):
	return render(request,'homepage.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="Email Already registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					password=request.POST['password'],
					)
				msg="User SignUp Successfully"
				return render(request,'signup.html',{'msg':msg})
			else:
				msg="Password & Confirm Password does not match"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request,'homepage.html')
			else:
				msg:"Invalid Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email not registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')		
