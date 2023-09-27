from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest,HttpResponse
from.models import Course,Trainer,Payment,Order
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
import uuid
from django.template.loader import render_to_string
from django.contrib.auth import authenticate,login,logout
import json
from django.views.decorators.csrf import csrf_exempt

def Login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['pwd']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)  
            username=user.username
            #return render(request,"Home.html",{'username':username})
            return redirect('home')

        else:
            messages.error(request," You are entered incorrect  Username or password.")
            return render(request,'login.html')
    return render(request,'login.html')

def Signup(request):
    if request.method=="POST":
        username=request.POST['username']
        Email=request.POST['email']
        password=request.POST['pwd']
        password2=request.POST['pass2']
        Qualification=request.POST['qualification']

        if User.objects.filter(username=username):
            messages.error(request,"USER NAME ALREADY EXIST, PLEASE TRY WITH ANOTHER USERNAME")
            return render(request,'signup.html')
        if User.objects.filter(email=Email):
            messages.error(request,"Email already exist!!")
            return render(request,'signup.html')
        if len(username)>10:
            messages.error(request,"Username must be  below 10 characters")
            return render(request,'signup.html')


        if password!=password2:
            messages.error(request,"Password didn't match")
            return render(request,'signup.html')

        if not username.isalnum():
            messages.error(request,"Username must be numeric")
            return render(request,'signup.html')
        myuser=User.objects.create_user(username,Email,password)
        myuser.save()
        messages.success(request,"Your account has been successfully created!!")
        return redirect('login')
    return render(request,'signup.html')

def Home(request):
        qset=Course.objects.all()
        return render(request,"Home.html",{'qset':qset})

def Trainers(request):
    trainer=Trainer.objects.all()
    return render(request,'trainer.html',{'trainer':trainer})


def logout(request):
    logout(request)
    return render(request,'login.html')


def Detail(request,rid):
    product=Course.objects.get(id=rid)
    context={}
    context['data']=product
    return render(request,'details.html',context)
    

def searching(request):
    if request.method=="GET":
        qset=request.GET['search']
        products=Course.objects.filter(Course_name__icontains=qset)
        return render(request,'search.html',{'products':products})
    elif Course.objects.filter(Course_name=qset):

        messages.error(request," You're entered Course is not available .")

    else:
        messages.error(request," You're entered Course is not available .")
 
        return render(request,"home.html")
    

def filters(request,x):
    if x=="1":
        qset=Course.objects.filter(Fee__gte=3000)

    else:
        qset=Course.objects.filter(Fee__lte=2000)
    
    
    content={}
    content['data']=qset
    return render(request,"filter.html",content)
 
@csrf_exempt
def payments(request,rid):
        qset=Course.objects.get(id=rid)
        content={}
        content['data']=qset
        #if User is not None:
        return render(request,'payment.html',content)
   
    

def generate_order():
    return str(uuid.uuid4().hex)[:10]  # Generate a random 10-character ID
# Usage
orderId = generate_order()
order = Order(orderId=generate_order())
order.save()

def Email(request):
    mail_subject="Payment Conformation"
    message=render_to_string('order_email.html',context={'user':request.user,'order':order,'title':'Enroll success'})
    from_email=settings.EMAIL_HOST_USER
    to_email=request.user.email
    send_email=EmailMessage(mail_subject,message,to=[to_email])
    send_email.send()
    return redirect('home')

    
'''def enroll_success(request):
    transid=request.GET.get('payment_id')
    return render(request,'paymentsuccess.html',{'transid':transid})'''



'''body=json.loads(request.body)
    order=Order.objects.get(user=request.user,order=body['orderId'])
    payment=Payment(
        payment_id=body['transactionId'],user=request.user,amount_paid=order.total,status=body['status'])
    payment.save()
    Order.payment=Payment
    Order.save() '''