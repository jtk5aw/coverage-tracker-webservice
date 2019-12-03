from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# WILL MOST LIKELY NOT GET USED FOR NOW
class Dorm(models.Model):
    name = models.CharField(max_length=50, default='Dorm')
    DORM_CHOICES = [
        ('FY', 'First Year'),
        ('UC', 'Upper Classmen'),
    ]
    dorm_type = models.CharField(
        max_length=2,
        choices=DORM_CHOICES,
        default='FY',
    )

class Staffer(models.Model):
    comp_id = models.CharField(max_length=10, default='xx0xx')
    STAFFER_CHOICES = [
        ('RA', 'Resident Advisor'),
        ('SR', 'Senior Resident'),
    ]
    staffer_type = models.CharField(
        max_length=2,
        choices=STAFFER_CHOICES,
        default='RA',
    ) # Can be RA or SR (could be Vice-Chair or Pro Staff in the future)
    name = models.CharField(max_length=50, default='Test Store')
    building = models.CharField(max_length=100, default='Fake Dorm') # Will be linked up with dorm strings from Firebase (hacky fix for now)
    on_coverage = models.BooleanField()
    phone_number = PhoneNumberField(default='5714395221')