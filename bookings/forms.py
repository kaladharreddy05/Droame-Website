from django import forms
from .models import Customer, Booking

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name', 'email', 'phone_number')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('drone_shot_name', 'customer')
