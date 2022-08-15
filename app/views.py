from email.mime import message
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact,Login,Booking
from django.contrib import messages 

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        
        con = Contact(name=name,email=email,number=number,message=message)
        con.save()
        return HttpResponse('THANKS FOR YOUR TIME WE WILL UPDATE YOU SOON...')
    return render(request,'index.html')

def problems(request,que_id=0):
    que = Contact.objects.all()
    if que_id:
        try:
            que_to_be_removed = Contact.objects.get(id=que_id)
            que_to_be_removed.delete()
        except:
            return HttpResponse("please give correct details")
    context = {
        'que':que
    }
            
    return render(request,'problems.html',context)
    
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        
        l = Login(name=name,password=password)
        l.save()
    
    return render(request,'index.html')


def booking(request):
    if request.method== 'POST':
        firstname= request.POST['firstname']
        lastname = request.POST['lastname']
        place = request.POST['place']
        number = request.POST['number']
        phone = request.POST['phone']
        
        book = Booking(firstname=firstname,lastname=lastname,place=place,number=number,phone=phone)
        book.save()
        return render(request,'index.html')
    return render(request,'booking.html')

