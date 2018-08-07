# Acrisure forms
from django.forms import ModelForm
#from django import forms
from acrisure.models import Account

# Account form
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
