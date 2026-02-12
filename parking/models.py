from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()

    class Meta:
        db_table = "customer"

    def __str__(self):
        return self.user.username

class ParkingOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parking_name = models.CharField(max_length=100)

    class Meta:
        db_table = "parking_owner"

    def __str__(self):
        return self.parking_name


class ParkingLocation(models.Model):
    ownerId = models.ForeignKey("ParkingOwner", on_delete=models.CASCADE)
    location_name = models.CharField(max_length=100)
    address = models.TextField()
    total_slots = models.IntegerField()

    class Meta:
        db_table = "parking_location"

    def __str__(self):
        return self.location_name

class ParkingSlot(models.Model):
    locationId = models.ForeignKey("ParkingLocation", on_delete=models.CASCADE)
    slot_number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = "parking_slot"

    def __str__(self):
        return self.slot_number


class Vehicle(models.Model):
    customerId = models.ForeignKey("Customer", on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)

    class Meta:
        db_table = "vehicle"

    def __str__(self):
        return self.vehicle_number


class Booking(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    customerId = models.ForeignKey("Customer", on_delete=models.CASCADE)
    parking_slotId = models.ForeignKey("ParkingSlot", on_delete=models.CASCADE)
    booking_date = models.DateField()
    duration = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "booking"

    def __str__(self):
        return f"Booking {self.id}"


class Payment(models.Model):
    PAYMENT_TYPE = (
        ('UPI', 'UPI'),
        ('CARD', 'CARD'),
        ('CASH', 'CASH'),
    )

    PAYMENT_STATUS = (
        ('success', 'Success'),
        ('failed', 'Failed'),
    )

    booking = models.OneToOneField("Booking", on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "payment"

    def __str__(self):
        return f"Payment {self.id}"


class Review(models.Model):
    customerId = models.ForeignKey("Customer", on_delete=models.CASCADE)
    parking_locationId = models.ForeignKey("ParkingLocation", on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = "review"

    def __str__(self):
        return f"Review {self.id}"


