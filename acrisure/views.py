from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
#from django.core.serializers import serialize
#from django.core import serializers

from .models import *
from .forms import AccountForm, CoverageForm, PolicyForm, VehicleForm, AccountSelector


# Login view @ index
def index(request):
    if request.method == "POST":
        """ Log in User """
        logout(request)
        username = request.POST["username"]
        password = request.POST["pass"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return HttpResponse("Todo username or password is wrong")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("dashboard"))
        return render(request, "acrisure/login.html")


@login_required(login_url='/')
def dashboard_view(request):
    """ Dashboard / Login Landing View / Main Page """

    # Generate blank forms
    accountform = AccountForm()
    coverageform = CoverageForm()
    policyform = PolicyForm()
    vehicleform = VehicleForm()
    accountselector = AccountSelector()

    # Create Template Context
    context = {
        'accountform': accountform,
        'coverageform': coverageform,
        'policyform': policyform,
        'vehicleform': vehicleform,
        'accountselector': accountselector,
    }

    return render(request, "acrisure/dashboard.html", context)


@login_required(login_url='/')
def add_client(request):
    if request.method == 'POST':
        # Generate form with data from the request
        accountform = AccountForm(request.POST)
        # Reference is now a bound instance with user data sent in POST
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if accountform.is_valid():
            accountform.save()
            return HttpResponseRedirect(reverse("dashboard"))

        # !!! This needs to be changed !!!
        return HttpResponse("Recieved unclean Form")
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url='/')
def add_coverage(request):
    if request.method == 'POST':
        # Generate form with data from the request
        coverageform = CoverageForm(request.POST)
        # Reference is now a bound instance with user data sent in POST
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if coverageform.is_valid():
            coverageform.save()
            return HttpResponseRedirect(reverse("dashboard"))

        # !!! This needs to be changed !!!
        return HttpResponse("Recieved unclean Form")
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url='/')
def add_policy(request):
    if request.method == 'POST':
        # Generate form with data from the request
        policyform = PolicyForm(request.POST)
        # Reference is now a bound instance with user data sent in POST
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if policyform.is_valid():
            policyform.save()
            return HttpResponseRedirect(reverse("dashboard"))

        # !!! This needs to be changed !!!
        return HttpResponse("Recieved unclean Form")
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url='/')
def add_vehicle(request):
    if request.method == 'POST':
        vehicleform = VehicleForm(request.POST)
        if vehicleform.is_valid():
            vehicleform.save()
            return HttpResponseRedirect(reverse("dashboard"))


        # !!! This needs to be changed !!!
        return HttpResponse("Recieved unclean Form")
    return HttpResponseRedirect(reverse("index"))


@login_required(login_url='/')
def policy_cancel(request):
    if request.method == 'POST':
        meta = int(request.POST.get('meta'))

        if meta == 0:
            id_accounts = request.POST.get('account_choice')
            print(dict(data=list(Policy.objects.filter(account=id_accounts).values('policy_number'))))
            return JsonResponse(dict(data=list(Policy.objects.filter(account=id_accounts).values('policy_number'))))
        elif meta == 1:
            id_cnx_pol = request.POST.get('cnx_policy_choice')
            new_expiration_date = request.POST.get('new_expiration_date')
            result = Policy.objects.filter(policy_number=id_cnx_pol).update(expiration_date=new_expiration_date)
            if result == 1:
                return JsonResponse({'success': True, 'exp': new_expiration_date})
            else:
                return JsonResponse({'success': False})
        else:
            return JsonResponse({'success': False})

    else:
        return HttpResponse("Todo get on policy_cancel")


# Logs user out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


""" Create profile object for each new user added via admin. """
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
