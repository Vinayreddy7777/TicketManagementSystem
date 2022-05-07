from django.shortcuts import render, redirect,get_object_or_404
#importing resources for messages.
from django.contrib import messages

#importing resources for search in search box.
from django.db.models import Q

from userapp.models import TicketModel


# Create your views here.
def admin_login(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        if name =='admin' and password =='admin':
           return redirect('admin_home')
        elif name =='admin@gmail.com' and password =='admin':
           return redirect('admin_home')
        else:
            messages.error(request, "Invalid Login") 
    return render(request,'admin-login.html')

def admin_home(request):
    raised_tickts=TicketModel.objects.all()
    return render(request,'admin-home.html',{'d':raised_tickts})


#Admin Update Backend Start.  
def accept_ticket(request,id):
    accept=get_object_or_404(TicketModel,ticket_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('admin_home')

def reject_ticket(request,id):
    reject=get_object_or_404(TicketModel,ticket_id=id)
    reject.status='Rejected'
    reject.save(update_fields=['status'])
    reject.save()
    return redirect('admin_home')
#Admin  Update Backend End.

