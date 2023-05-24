from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random
from .pdf import html2pdf 

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
					house=request.POST['house'],
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
					event=Events.objects.all()
					notice=Notice.objects.all()
					return render(request,'member-profile.html',{'event':event,'notice':notice})
				else:
					msg="Invalid password"
					return render(request,'login.html',{'msg':msg})

			elif user.usertype=="Chairman":
				if user.password==request.POST['password']:
					request.session['email']=user.email
					request.session['fname']=user.fname
					notice=Notice.objects.all()
					event=Events.objects.all()
					return render(request,'chairmanhomepage.html',{'notice':notice,'event':event})
				else:
					msg="Invalid password"
					return render(request,'login.html',{'msg':msg})

			elif user.usertype=="Watchman":
				if user.password==request.POST['password']:
					request.session['email']=user.email
					request.session['fname']=user.fname
					# requst.session['profile_pic']=user.profile_pic.url
					event=Events.objects.all()
					visitor=Visitor.objects.all()
					return render(request,'watchmanhomepage.html',{'event':event,'visitor':visitor})
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

# Chairman Working

def chairmanprofile(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if request.method=="POST":
			user.fname=request.POST['fname']
			user.lname=request.POST['lname']
			user.email=request.POST['email']
			user.mobile=request.POST['mobile']
			user.save()
			msg="Profile Updated Successfully"
			request.session['email']=user.email
			return render(request,'updatechairmanprofile.html',{'user':user,'msg':msg})
		else:
			return render(request,'updatechairmanprofile.html',{'user':user})
	except:
		msg="Please Login To see your profile"
		return render(request,'login.html',{'msg':msg})
def chairmanhome(request):
	if request.method=="GET":
		notice=Notice.objects.all()
		event=Events.objects.all()
		return render(request,'chairmanhomepage.html',{'notice':notice,'event':event})

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

def edit_notice(request,pk):
	notice=Notice.objects.get(pk=pk)
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

def delete(request,pk):
	event=Events.objects.get(pk=pk)
	event.delete()
	return redirect('chairmanhome')

def delete_notice(request,pk):
	notice=Notice.objects.get(pk=pk)
	notice.delete()
	return redirect('chairmanhome')

def chairmancomplain(request):
	if request.method=="POST":
		Watchman.objects.create(
			name=request.POST['name'],
			house=request.POST['house'],
			mobile=request.POST['mobile'],
			complain=request.POST['complain'],
			date=request.POST['date'],
			status=request.POST['status'],
			)
		complain=Watchman.objects.all()
		return render(request,'chairmancomplainpage.html',{'complain':complain})
	else:
		complain=Watchman.objects.all()
		return render(request,'chairmancomplainpage.html',{'complain':complain})

def chairmanseecomplain(request):
	if request.method=="GET":
		complain=Watchman.objects.all()
		return render(request,'chairmanseecomplainpage.html',{'complain':complain})

def society_members(request):
	if request.method=="GET":
		user=User.objects.all()
		return render(request,'society-member-list.html',{'user':user})

def pdf(request):
	pdf= html2pdf('society-member-list.html')
	return HttpResponse(pdf,content_type="application/pdf")

def maintainance_amount(request):
	if request.method=="POST":
		Chairman.objects.create(maintainance=request.POST['amount'],)
		return render(request,'maintainance.html')
	else:
		return render(request,'maintainance.html')

# def edit_amount(request):
# 	if request.method=="POST":
# 		amount=Chairman.objects.get('maintainance')
# 		amount.amount=request.POST['amount']
# 		return render(request,'change-maintainance.html')
# 	else:
# 		return render(request,'change-maintainance.html')

# Watchman Working


def watchmanprofile(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if request.method=="POST":
			user.fname=request.POST['fname']
			user.lname=request.POST['lname']
			user.email=request.POST['email']
			user.mobile=request.POST['mobile']
			user.save()
			msg="Profile Updated Successfully"
			request.session['email']=user.email
			return render(request,'updatewatchmanprofile.html',{'user':user,'msg':msg})
		else:
			return render(request,'updatewatchmanprofile.html',{'user':user})
	except:
		msg="Please Login To see your profile"
		return render(request,'login.html',{'msg':msg})

def visitor(request):
	if request.method=="POST":
		Visitor.objects.create(
			name=request.POST['name'],
			house=request.POST['house'],
			mobile=request.POST['mobile'],
			purpose=request.POST['purpose'],
			date=request.POST['date'],
			vehical=request.POST['vehical'],
			)
		event=Events.objects.all()
		visitor=Visitor.objects.all()
		return render(request,'watchmanhomepage.html',{'visitor':visitor,'event':event})
	else:
		return render(request,'visitor-registration.html')

def notice_view_watchman(request):
	if request.method=="GET":
		notice=Notice.objects.all()
		return render(request,'notice-view-watchman.html',{'notice':notice})
	else:
		visitor=Visitor.objects.all()
		return render(request,'watchmanhomepage.html',{'visitor':visitor})

def watchmanhome(request):
	if request.method=="GET":
		visitor=Visitor.objects.all()
		return render(request,'watchmanhomepage.html',{'visitor':visitor})

def event_view_watchman(request):
	if request.method=="GET":
		event=Events.objects.all()
		return render(request,'event-view-watchman.html',{'event':event})
	else:
		visitor=Visitor.objects.all()
		return render(request,'watchmanhomepage.html',{'visitor':visitor})

def complain(request):
	if request.method=="POST":
		Watchman.objects.create(
			name=request.POST['name'],
			house=request.POST['house'],
			mobile=request.POST['mobile'],
			complain=request.POST['complain'],
			date=request.POST['date'],
			status=request.POST['status'],
			)
		complain=Watchman.objects.all()
		membercomplain=Watchman.objects.all()
		return render(request,'complainpage.html',{'complain':complain,'membercomplain':membercomplain})
	else:
		complain=Watchman.objects.all()
		membercomplain=Watchman.objects.all()
		return render(request,'complainpage.html',{'complain':complain,'membercomplain':membercomplain})

def view_complain_watchman(request):
	if request.method=="GET":
		user=User.objects.get(email=request.session['email'])
		complain=Watchman.objects.all()
		membercomplain=Watchman.objects.all()
		return render(request,'watchmanseecomplainpage.html',{'complain':complain,'membercomplain':membercomplain})


def complete_task(request):
	id=int(request.POST['id'])
	task=Watchman.objects.get(pk=id)
	task.status="completed"
	task.save()
	return redirect('watchmanhome')

# Society members

def member_list(request):
	if request.method=="GET":
		user=User.objects.filter(usertype="society-member")
		return render(request,'member-list.html',{'user':user})

def member_profile(request):
	if request.method=="GET":
		event=Events.objects.all()
		notice=Notice.objects.all()
		return render(request,'member-profile.html',{'event':event,'notice':notice})

def watchman_details(request):
	if request.method=="GET":
		user=User.objects.filter(usertype="Watchman")
		return render(request,'member-list.html',{'user':user})

def raise_complain(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		Watchman.objects.create(
			name=request.POST['name'],
			house=request.POST['house'],
			mobile=request.POST['mobile'],
			complain=request.POST['complain'],
			date=request.POST['date'],
			status=request.POST['status'],
			)
		membercomplain=Watchman.objects.all()
		return render(request,'member-complainpage.html',{'membercomplain':membercomplain})
	else:
		complain=Watchman.objects.all()
		return render(request,'member-complainpage.html',{'complain':complain})

def membercomplain(request,pk):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		membercomplain=Watchman.objects.get(pk=pk)
		return render(request,'see-complain.html',{'membercomplain':membercomplain})