from django.db import models
from App_Login.models import user_registration
from App_Add_Flat.models import Add_Flat
from App_Login.models import CreateUser

# Create your models here.


class Booking(models.Model):
    renter = models.ForeignKey(CreateUser, related_name='renter_info', on_delete=models.CASCADE)
    info_flat = models.ForeignKey(Add_Flat, related_name='flat_info', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.renter
