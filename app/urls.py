from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index , name='index'),
    path('problems',views.problems , name='problem'),
    path('login',views.login, name='login'),
    path('booking',views.booking,name='booking'),
]