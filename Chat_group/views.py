import email
from typing import MutableSequence
from django.core.checks import messages
from django.http import request
from django.shortcuts import redirect, render,HttpResponse
from Chat_group.models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from datetime import timezone
import smtplib
import datetime
from email.message import EmailMessage
from random import choice
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def hloo(request):
    if request.user.is_authenticated:
        return render(request,'index1.html')
    else:
        hk=0
        return render(request,'Signup.html', {'hkss':hk}) 

#generating random unicode    
def generate_random_unicode():
        # logic to generate code
        varsptoken = ''
        alphas = ['-', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(26):
            alphas.append(chr(65+i))
            alphas.append(chr(97+i))
        for i in range(89):
            varsptoken += choice(alphas)

        return varsptoken

# mail for account verification
def send_mail(to, personalcode):
        # logic to send mail to user
    sender_mail = f"{settings.MAIL_SENDER}"
    password_sender = f"{settings.PASS_MAIL}"
    message = EmailMessage()
    message['To'] = to
    message['From'] = sender_mail
    message['Subject'] = "Welcome to Fb Clone"
    message.set_content(
        f"Hello User welcome to FbClone.com Your one time login link is\n {settings.SITE_URL}/verify/{personalcode} \nvalid for next 15 minutes.")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(sender_mail, password_sender)
        server.send_message(message)
        return True         # success 
    except:
        return False   

# Sent on new device login
def new_device_mail(to):
        # logic to send mail to user
    sender_mail = f"{settings.MAIL_SENDER}"
    password_sender = f"{settings.PASS_MAIL}"
    message = EmailMessage()
    message['To'] = to
    message['From'] = sender_mail
    message['Subject'] = "New Device Login alert!!"
    message.set_content(
        f"Your account logined into new device if it wasn't you we  recommands you to please reset your password")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(sender_mail, password_sender)
        server.send_message(message)
        return True         # success 
    except:
        return False   

# Signup View   
@csrf_exempt
def signup(request):
    if request.method=='POST':
        data = json.loads(request.body)
        first_name= data.get("fname")
        last_name= data.get("lname")
        username= data.get("username")
        email= data.get("email")
        passw= data.get("pass")
        passw1= data.get("pass1")

        if(first_name=='' or last_name=='' or username=='' or email=='' or passw==''):
            return JsonResponse({'status':400,'message':'Please fill out all the fields!!'})

        if passw==passw1:
            if User.objects.filter(username=username).exists():
                return JsonResponse({'status':400,'message':'Username aleady exists!!'})
            elif User.objects.filter(email=email).exists():
                return JsonResponse({'status':400,'message':'Email already exists!!'})
            else:
                personalcode = generate_random_unicode()
                mytimecalculator = 0
                while(len(profile_details.objects.filter(unicode=personalcode))):
                    personalcode = generate_random_unicode()
                    mytimecalculator += 1
                    if mytimecalculator > 10000:
                        pass 

                status = send_mail(email, personalcode)
                user=User.objects.create_user(username=username, password=passw, email=email, first_name=first_name,last_name=last_name)
                user.save();
                hkk=1
                upes = profile_details(user=user, terimail=email,u_nm= username,fstname=first_name,secname=last_name,
                            unicode=personalcode, timestamp=datetime.datetime.now(timezone.utc))
                upes.save()
                return JsonResponse({'status':200,'message':'Verification link has been sent to your email please check inbox!!'})
        else:
            return JsonResponse({'status':400,'message':'Password did not matched !!'})
    else:
        return JsonResponse({'status':400,'message':''})

#Login_view    
@csrf_exempt
def login(request):
    if request.method=='POST':
        data = json.loads(request.body)
        username= data.get("username")
        password= data.get("pass")

        if(username=='' or password==''):
            return JsonResponse({'status':400,'message':'Please fill out all fields !!'})
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            datas = profile_details.objects.filter(user=user)
            for data in datas:
                if not data.verified:
                    return JsonResponse({'status':400,'message':'Your mail is not verified...'})
            auth.login(request,user)
            return JsonResponse({'status':200,'message':'success'})
        else:
            return JsonResponse({'status':400,'message':'User does not exists !!'})
    else:
        return render(request,'Signup.html')

def shsgn(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        hk=0
        return render(request,'Signup.html', {'hkss':hk})

def shlgn(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        hk=1
        return render(request,'Signup.html', {'hkss':hk})

def join_grp(request):
    if request.method=='POST':
        name=request.POST.get('grp_name')
        grp_obj=Chat_Groups.objects.get(name=name)
        if grp_obj is not None:
            if(request.user in grp_obj.user.all()):
              dd=grp_obj.id
            else:  
                grp_obj.user.add(request.user)
                grp_obj.members = grp_obj.members+1
                grp_obj.save()     
            dd=grp_obj.id
            Chat_history=Chat.objects.filter(group=dd)
            return render(request,'index.html',{'grpname':name,'chate':Chat_history})
        else:
            print('errer')
            return render(request,'index1.html')


