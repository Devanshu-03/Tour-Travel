from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    message = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s %s %s"%(self.id,self.name,self.email,self.number,self.message)
    
    
class Login(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    
    def __str__(self):
        return "%s %s "%(self.name,self.password)
    
    
class Booking(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    
    def __str__(self):
        return "%s %s %s %s %s"%(self.firstname,self.lastname,self.place,self.number,self.phone)
    