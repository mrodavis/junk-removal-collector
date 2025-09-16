from django.urls import path
from . import views

urlpatterns = [
    path("", views.JobListView.as_view(), name="job_list"),
    path("jobs/<int:pk>/", views.JobDetailView.as_view(), name="job_detail"),
    path("jobs/create/", views.JobCreateView.as_view(), name="job_create"),
    path("jobs/<int:pk>/update/", views.JobUpdateView.as_view(), name="job_update"),
    path("jobs/<int:pk>/delete/", views.JobDeleteView.as_view(), name="job_delete"),

    path("haulers/", views.HaulerListView.as_view(), name="hauler_list"),
    path("haulers/<int:pk>/", views.HaulerDetailView.as_view(), name="hauler_detail"),
]
