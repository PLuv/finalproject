# Acrisure models
from djmoney.models.fields import MoneyField
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# User profile class to manipulate user attributes outside of the authenticate system
# Profile = Employee/users * HR/Management(superusers)
# Todo decide if user should be onetoone or foreign key
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

# Company name choices
class Company(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name}"


# Account(client)
class Account(models.Model):
    # name = business name
    name = models.CharField(max_length = 50)
    # owner's name set to max_length 35 per UK Gov standards for names http://webarchive.nationalarchives.gov.uk/20100407173424/http://www.cabinetoffice.gov.uk/govtalk/schemasstandards/e-gif/datastandards.aspx
    # http://webarchive.nationalarchives.gov.uk/+/http://www.cabinetoffice.gov.uk/media/254290/GDS%20Catalogue%20Vol%202.pdf
    owner = models.CharField(max_length = 35)
    phone = models.CharField(max_length = 11, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length = 75)

    def __str__(self):
        return f"{self.name}"


# Vehicle class
class Vehicle(models.Model):
    year = models.CharField(max_length = 35)
    make = models.CharField(max_length = 20)
    model = models.CharField(max_length = 20)
    vin = models.CharField(max_length = 17)
    ded = MoneyField(max_digits=5, decimal_places=0, default_currency='USD')
    value = MoneyField(max_digits=8, decimal_places=2, default_currency='USD')

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


# Coverage options
class Coverage(models.Model):
    liability = models.CharField(max_length = 30)
    symbol = models.IntegerField()
    pip = models.CharField(max_length = 6)
    um = models.CharField(max_length = 15)
    ded = MoneyField(max_digits=7, decimal_places=0, default_currency='USD')

    def __str__(self):
        return f"Liability: {self.liability} UM: {self.um} Ded:{self.ded}"


# Policy class
class Policy(models.Model):
    PTYPE_CHOICES = (
        ('CAU', 'Commercial Auto'),
        ('GL', 'General Liability'),
    )
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    ptype = models.CharField(max_length = 3, choices=PTYPE_CHOICES)
    policy_number = models.CharField(max_length = 20)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    effective_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)
    coverages = models.ForeignKey(Coverage, on_delete=models.PROTECT, null=True, blank=True)
    vehicles = models.ForeignKey(Vehicle, on_delete=models.PROTECT, null=True, blank=True)