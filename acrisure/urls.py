from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("out", views.logout_view, name="out"),
    path("add_client", views.add_client, name="add_client"),
    path("add_coverage", views.add_coverage, name="add_coverage"),
    path("add_policy", views.add_policy, name="add_policy"),
    path("add_vehicle", views.add_vehicle, name="add_vehicle"),
    path("policy_cancel", views.policy_cancel, name="policy_cancel"),
    path("veh_delete", views.veh_delete, name="veh_delete"),
]
