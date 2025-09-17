from django.urls import path
from . import views 
from .views import SignUpView

urlpatterns = [
    # Jobs
    path("", views.JobListView.as_view(), name="job_list"),
    path("jobs/<int:pk>/", views.JobDetailView.as_view(), name="job_detail"),
    path("jobs/create/", views.JobCreateView.as_view(), name="job_create"),
    path("jobs/<int:pk>/update/", views.JobUpdateView.as_view(), name="job_update"),
    path("jobs/<int:pk>/delete/", views.JobDeleteView.as_view(), name="job_delete"),

    # Haulers
    path("haulers/", views.HaulerListView.as_view(), name="hauler_list"),
    path("haulers/<int:pk>/", views.HaulerDetailView.as_view(), name="hauler_detail"),

    # Equipment
    path("equipment/", views.EquipmentListView.as_view(), name="equipment_list"),
    path("equipment/<int:pk>/", views.EquipmentDetailView.as_view(), name="equipment_detail"),
    path("equipment/create/", views.EquipmentCreateView.as_view(), name="equipment_create"),
    path("equipment/<int:pk>/update/", views.EquipmentUpdateView.as_view(), name="equipment_update"),
    path("equipment/<int:pk>/delete/", views.EquipmentDeleteView.as_view(), name="equipment_delete"),

    # Disposal Details (linked to Job)
    path("jobs/<int:pk>/disposal/add/", views.DisposalCreateView.as_view(), name="disposal_create"),
    path("disposals/<int:pk>/update/", views.DisposalUpdateView.as_view(), name="disposal_update"),
    path("disposals/<int:pk>/delete/", views.DisposalDeleteView.as_view(), name="disposal_delete"),

    path("accounts/signup/", SignUpView.as_view(), name="signup"),
]
