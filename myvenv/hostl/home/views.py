from django.shortcuts import render
from django .http import HttpResponse

from .forms import BookingForm
# Create your views here.
from .models import Department,doctors,booking

def index(request):
   return render(request,'index.html')
def about(request):
   return render(request,'about.html')
def booking(request):
   if request.method=='POST':
      form=BookingForm(request.POST)
      if form.is_valid():
         form.save()
         return render(request,'confimations.html')
   form=BookingForm()
   dict_form={
      'form':form
   }
   
   return render(request,'booking.html',dict_form)
def doctorss(request):
   dict_doc={
      'doct':doctors.objects.all() 
   }
   return render(request,'doctors.html',dict_doc)

def department(request):
   dict_dept={
      'dept':Department.objects.all()
   }
   return render(request,'department.html',dict_dept)
   
def contact(request):
    return render(request,'contact.html')
