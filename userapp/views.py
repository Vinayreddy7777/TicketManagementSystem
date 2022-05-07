from django.shortcuts import render, redirect, get_object_or_404
from userapp.models import  UserModel, TicketModel

#importing resources for messages.
from django.contrib import messages

#importing resources for search in search box.
from django.db.models import Q



# Create your views here.



def user_login(request):
    if request.method=="POST":
        name=request.POST.get("email")
        password=request.POST.get("password")
        try:
            check=UserModel.objects.get(email=name,password=password)
            request.session["user_id"]=check.user_id
            return redirect('user_home')
        except:
            messages.error(request,'Invalid Login')
    return render(request,'user-login.html')




def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
                
        if UserModel.objects.filter(email=email).exists():
            messages.error (request, "Email already exist")
        else:
            user=UserModel.objects.create(username=username,mobile=mobile,email=email,password=password)
            user.save()
            messages.success(request, "Account created successful")

    return render(request,'user-register.html')

def user_home(request):
    user_id = request.session["user_id"]
    user_register=UserModel.objects.filter(user_id=user_id)
    if request.method == "POST":
        name= request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        user=UserModel.objects.get(user_id=user_id)
        
        user=TicketModel.objects.create(name=name,email=email,subject=subject,message=message,user=user)
        if user:    
            messages.success(request, "Ticket Raised Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")
    return render(request,'user-home.html',{'d':user_register})

def user_view(request):
    user_id = request.session["user_id"]
    raised_tickets=TicketModel.objects.filter(user=user_id, status="Pending")
    return render(request,'user-view.html',{'d':raised_tickets})

def user_edit(request,id):
    edit=TicketModel.objects.filter(ticket_id=id) 
    obj = get_object_or_404(TicketModel,ticket_id=id)
    if request.method == "POST":
        name= request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        obj.name=name
        obj.email=email
        obj.subject=subject
        obj.message=message
        obj.save()
        
        if obj:    
            messages.success(request, "Ticket Updated Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")
    return render(request,'user-edit.html',{'d': edit})

def user_status(request):
    user_id = request.session["user_id"]
    raised_tickets=TicketModel.objects.filter(user=user_id)
    return render(request,'user-status.html',{'d':raised_tickets})
