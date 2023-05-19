from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.

def index(request):
	return render(request,'login.html')

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
					usertype=request.POST['usertype'],
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
			user=User.objects.get(email=request.POST['email'])
			if user.usertype=="society-member":
				if user.password==request.POST['password']:
					request.session['email']=user.email
					request.session['fname']=user.fname
					# requst.session['profile_pic']=user.profile_pic.url

					return render(request,'home.html')
				else:
					msg="Invalid password"
					return render(request,'login.html',{'msg':msg})

			elif user.usertype=="Chairman":
				if user.password==request.POST['password']:
					request.session['email']=user.email
					request.session['fname']=user.fname
					# requst.session['profile_pic']=user.profile_pic.url
					notice=Notice.objects.all()
					return render(request,'chairmanhomepage.html',{'notice':notice})
				else:
					msg="Invalid password"
					return render(request,'login.html',{'msg':msg})

			else:
				msg="Invalid password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email not registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')		

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		# del request.session['profile_pic']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def profile(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if request.method=="POST":
			user.fname=request.POST['fname']
			user.lname=request.POST['lname']
			user.email=request.POST['email']
			user.mobile=request.POST['mobile']
			# try:
			# 	user.profile_pic=request.FILES['profile_pic']
			# except:
			# 	pass
			user.save()
			msg="Profile Updated Successfully"
			request.session['email']=user.email
			return render(request,'update.html',{'user':user,'msg':msg})
		else:
			return render(request,'update.html',{'user':user})
	except:
		msg="Please Login To see your profile"
		return render(request,'login.html',{'msg':msg})

def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP for Forgot Password'
			message = 'Hello ' + user.fname + ', Your OTP for forgot password is: '+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email,]
			send_mail( subject, message, email_from, recipient_list)
			return render(request,'otp.html',{'email':user.email,'otp':otp})

		except:
			msg="Email not registered"
			return render(request,'forgot-password.html',{'msg':msg})
	else:
		return render(request,'forgot-password.html')

def verify_otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']

	if otp==uotp:
		return render(request,'new-password.html',{'email':email})

	else:
		msg:"Please Enter Valid OTP"
		return render(request,'otp.html',{'email':email,'msg':msg})

def new_password(request):
	email=request.POST['email']
	np=request.POST['npassword']
	cnp=request.POST['cnpassword']

	if np==cnp:
		user=User.objects.get(email=email)
		user.password=np
		user.save()
		msg="Your Password has been changed successfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="New Password and Confirm new password does not matched"
		return render(request,'new-password.html') 

def notice(request):
	if request.method=="POST":
		Notice.objects.create(
			date=request.POST['date'],
			event=request.POST['notice'],
			)
		notice=Notice.objects.all()
		event=Events.objects.all()
		return render(request,'chairmanhomepage.html',{'notice':notice,'event':event})
	else:
		return render(request,'notice.html')

def notice_view(request):
	if request.method=="GET":
		notice=Notice.objects.all()
		return render(request,'notice-view.html',{'notice':notice})
	else:
		return render(request,'chairmanhomepage.html')

def chairmanhome(request):
	if request.method=="GET":
		notice=Notice.objects.all()
		event=Events.objects.all()
		return render(request,'chairmanhomepage.html',{'notice':notice,'event':event})

def edit_notice(request):
	notice=Notice.objects.all()
	if request.method=="POST":
		notice.date=request.POST['date']
		notice.event=request.POST['notice']
		notice.save()
		return redirect('chairmanhome')
	else:
		notice=Notice.objects.all()
		return render(request,'notice-edit.html')

def add_event(request):
	if request.method=="POST":
		Events.objects.create(
			date=request.POST['date'],
			event=request.POST['event'],
			)
		event=Events.objects.all()
		notice=Notice.objects.all()
		return render(request,'chairmanhomepage.html',{'event':event,'notice':notice})
	else:
		event=Events.objects.all()
		notice=Notice.objects.all()
		return render(request,'add-event.html',{'event':event,'notice':notice})

def event_view(request):
	if request.method=="GET":
		event=Events.objects.all()
		return render(request,'event-view.html',{'event':event})
	else:
		return render(request,'chairmanhomepage.html')
