from django.contrib import admin
from .models import Profile, Company, Account, Vehicle, Coverage, Policy

# Register your models here.
admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(Account)
admin.site.register(Vehicle)
admin.site.register(Coverage)
admin.site.register(Policy)