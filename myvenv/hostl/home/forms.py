


from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import booking
from django.forms import ModelForm


class dateinput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields='__all__'
        
        widgets={
            'booking_date':dateinput(),
        }
        labels={
            'p_name':'patient name:',
            'p_phone':'patient phone:',
            'p_email':'panient email:',
            'doc_name':'Doctor Name:',
            'booking_date':"Booking Date:"
        }

     
           