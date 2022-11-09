from django.contrib import admin
from App_Flat_Booking.models import Booking


class Booking_Admin(admin.ModelAdmin):
    list_display = ['renter', 'info_flat', 'created']

    class Meta:
        model = Booking


# Register your models here.
admin.site.register(Booking, Booking_Admin)
