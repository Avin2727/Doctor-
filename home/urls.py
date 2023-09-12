from django.urls import path, include
from .import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('About', views.About, name='About'),
    path('booking', views.booking, name='booking'),
    path('doctors', views.Doctor, name='doctors'),
    path('contact', views.contact, name='contact'),
    path('department', views.Departments, name='Department'),
]
