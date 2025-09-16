from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Job, Hauler

# JOB VIEWS
class JobListView(ListView):
    model = Job
    template_name = "jobs/job_list.html"
    context_object_name = "jobs"

class JobDetailView(DetailView):
    model = Job
    template_name = "jobs/job_detail.html"

class JobCreateView(CreateView):
    model = Job
    template_name = "jobs/job_form.html"
    fields = ["customer", "description", "address", "date", "status"]
    success_url = reverse_lazy("job_list")

class JobUpdateView(UpdateView):
    model = Job
    template_name = "jobs/job_form.html"
    fields = ["customer", "description", "address", "date", "status"]
    success_url = reverse_lazy("job_list")

class JobDeleteView(DeleteView):
    model = Job
    template_name = "jobs/job_confirm_delete.html"
    success_url = reverse_lazy("job_list")


# HAULER VIEWS
class HaulerListView(ListView):
    model = Hauler
    template_name = "jobs/hauler_list.html"
    context_object_name = "haulers"

class HaulerDetailView(DetailView):
    model = Hauler
    template_name = "jobs/hauler_detail.html"
