from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *
#from .forms import *

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


# dashboard = landing page when user logs in.
def dashboard_view(request):
    return render(request, "acrisure/dashboard.html")

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
