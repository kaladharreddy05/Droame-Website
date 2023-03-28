from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(auto_now_add=True)
    drone_shot_name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
