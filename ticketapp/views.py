from django.shortcuts import render
from .models import Signup,Admin,Ticket
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def usersignup(request):
    return render(request,'usersignup')

def forget_pass(request):
    return render(request,'forget_pass.html')

@csrf_exempt
def validate_username(request):
    contxt={}
    if request.method=="POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        contact = request.POST.get('contact')
        address=request.POST.get('address')
        city=request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        # profile_picture=request.FILES('profile_picture')

        emp = Signup.objects.create(name=name, username=username, email=email,password=pwd,contact=contact,
                                    address=address,city=city,zipcode=zipcode)

        emp.save()

        request.session['email']=email

    return JsonResponse({"email":email,"success":True})

def userlogin(request):
    return render(request,'userlogin.html')

@csrf_exempt
def validate(request):
    dict={}
    if request.method=="POST":
        email = request.POST.get('email')
        get_pwd = request.POST.get('pwd')
        data = Signup.objects.get(email=email)
        email=data.email
        pwd=data.password
        if(get_pwd==pwd):
            request.session['email'] = email
            return JsonResponse({"email": email, "success": True})
        else:
            print("ppppppppp")
            return JsonResponse({"success": False})
def userhome(request):
    return render(request,'userhome.html')


def adminlogin(request):
    return render(request,'adminlogin.html')

@csrf_exempt
def my_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    data = Admin.objects.get(username=username)
    pwd=data.password
    if(password==pwd):
        print("success")
        return JsonResponse({"username": username, "success": True})
    else:
        print("invalid")
        return JsonResponse({"success": False})


    # pwd=pwd.split('$')
    # salt=pwd[1]
    # hsh=pwd[2]
    # print(salt)
    # print(hsh)
    # if (hsh==hashlib.sha1(salt+password).hexdigest()):
    #     print("Sucsess")
    # else:
    #     print("Not suceess"
def adminhome(request):
    return render(request,'adminhome.html')
@csrf_exempt
def new2(request):
    if request.method=='POST':
        get_email=request.POST.get("email")

    reset_pass1=Signup.objects.get(email=get_email)

    reset_pass=reset_pass1.password
    emailid=reset_pass1.email

    send_mail('Password email', str(reset_pass), 'shivam.mittal38@gmail.com', [emailid])

    return JsonResponse({"success": True,})



def adminload(requset):
        ticket_list = []
        data = Ticket.objects.all()
        if requset.method=="GET":
            for i in data:
                contxt={
                    'id':i.ticket_id,
                    'catagory':i.catagory,
                    'subject':i.subject,
                    'description':i.description
                }
                ticket_list.append(contxt)

        return JsonResponse({"success": True, 'ticket_list':ticket_list})



