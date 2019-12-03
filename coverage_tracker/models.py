from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

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
    building = models.ForeignKey(Dorm, on_delete=models.PROTECT)
    on_coverage = models.BooleanField()
    phone_number = PhoneNumberField()