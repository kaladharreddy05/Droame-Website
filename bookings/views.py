from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Customer, Booking
from .forms import CustomerForm, BookingForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'bookings/customer_list.html', {'customers': customers})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'bookings/customer_detail.html', {'customer': customer})

def index(request):
    customers = Customer.objects.all()
    bookings = Booking.objects.all()
    return render(request, 'bookings/index.html', {'customers': customers, 'bookings':bookings})

def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('index')
    else:
        form = CustomerForm()
    return render(request, 'bookings/customer_edit.html', {'form': form})

def customer_edit(request, id):
    customer = get_object_or_404(Customer, customer_id=id)
    if request.method == "POST":
        if request.POST.get('customer_name') and request.POST.get('email') and request.POST.get('phone_number'):
            customer.customer_name= request.POST.get('customer_name')
            customer.email= request.POST.get('email')
            customer.phone_number= request.POST.get('phone_number')
            customer.save()
            return redirect('index')  
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'bookings/customer_edit.html', {'customer': customer})

def customer_delete(request, id):
    customer = get_object_or_404(Customer, customer_id=id)
    customer.delete()
    return redirect('index')

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def booking_detail(request, id):
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

def booking_new(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        booking = Booking()
        booking.drone_shot_name= request.POST.get('drone_shot_name')
        index = request.POST.get('customer_id')
        booking.customer = get_object_or_404(Customer, customer_id=index)
        booking.created_time = timezone.now()
        booking.save()
        return redirect('index') 
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_edit.html', {'form': form,'customers':customers})

def booking_edit(request, id):
    booking = get_object_or_404(Booking, booking_id=id)
    customers = Customer.objects.all()
    if request.method == "POST":
        booking.drone_shot_name= request.POST.get('drone_shot_name')
        index = request.POST.get('customer_id')
        booking.customer = get_object_or_404(Customer, customer_id=index)
        booking.created_time = timezone.now()
        booking.save()
        return redirect('index') 
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_edit.html', {'booking': booking, 'customers':customers})

def booking_delete(request, id):
    booking = get_object_or_404(Booking, booking_id=id)
    booking.delete()
    return redirect('index')

