# Acrisure forms
from djmoney.models.fields import MoneyField
from django.forms import ModelForm, Textarea, ModelChoiceField
from django import forms
from acrisure.models import *

# Account form
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        widgets = {
            'address': Textarea(attrs={'cols': 60, 'rows': 5}),
        }


# Coverage form
class CoverageForm(ModelForm):
    class Meta:
        model = Coverage
        fields = '__all__'


# Policy form
class PolicyForm(ModelForm):
    class Meta:
        model = Policy
        fields = '__all__'

# Policy selector form
class PolicySelector(forms.Form):
    policy = ModelChoiceField(queryset=Policy.objects.all())


# Vehicle form
class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'