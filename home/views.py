from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from .forms import BookingForm
from .models import Department, doctor


# Create your views here.

def index(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'About.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    else:
        form = BookingForm()
    
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)


def Doctor(request):
    dict_docs = {
       'Doctor': doctor.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)


def contact(request):
    return render(request, 'contact.html')

      
def Departments(request):
    dict_dep={
        'dep': Department.objects.all()
    }
    return render(request,'department.html',dict_dep)