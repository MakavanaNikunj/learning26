from django.contrib import admin
from .models import Customer,ParkingOwner,ParkingLocation,ParkingSlot,Vehicle,Booking,Payment,Review

# Register your models here.


admin.site.register(Customer)
admin.site.register(ParkingOwner)
admin.site.register(ParkingLocation)
admin.site.register(ParkingSlot)
admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)

