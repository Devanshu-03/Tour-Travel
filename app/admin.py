from django.contrib import admin
from .models import Contact,Login,Booking
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' ,'email', 'number', 'message')
    
@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id','name','password')
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','place','number','phone')


    
    
