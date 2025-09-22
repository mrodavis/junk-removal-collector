from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Job, Hauler, Equipment, DisposalDetails

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

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
    fields = ["customer", "description", "address", "date", "status", "haulers"]
    success_url = reverse_lazy("job_list")

    def get_initial(self):
        initial = super().get_initial()
        customer_id = self.request.GET.get("customer")
        if customer_id:
            initial["customer"] = customer_id
        return initial

class JobUpdateView(UpdateView):
    model = Job
    template_name = "jobs/job_form.html"
    fields = ["customer", "description", "address", "date", "status", "haulers"]
    success_url = reverse_lazy("job_list")

class JobDeleteView(DeleteView):
    model = Job
    template_name = "jobs/job_confirm_delete.html"
    success_url = reverse_lazy("job_list")


# HAULER VIEWS
class HaulerListView(ListView):
    model = Hauler
    template_name = "haulers/hauler_list.html"
    context_object_name = "haulers"

class HaulerDetailView(DetailView):
    model = Hauler
    template_name = "haulers/hauler_detail.html"

class HaulerCreateView(CreateView):
    model = Hauler
    template_name = "haulers/hauler_form.html"
    fields = ["name", "phone", "email"]  # adjust fields to match your model
    success_url = reverse_lazy("hauler_list")

class HaulerUpdateView(UpdateView):
    model = Hauler
    template_name = "haulers/hauler_form.html"
    fields = ["name", "phone", "email"]  # adjust fields to match your model
    success_url = reverse_lazy("hauler_list")

class HaulerDeleteView(DeleteView):
    model = Hauler
    template_name = "haulers/hauler_confirm_delete.html"
    success_url = reverse_lazy("hauler_list")



# EQUIPMENT VIEWS
class EquipmentListView(ListView):
    model = Equipment
    template_name = "equipment/equipment_list.html"
    context_object_name = "equipment"

class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = "equipment/equipment_detail.html"

class EquipmentCreateView(CreateView):
    model = Equipment
    template_name = "equipment/equipment_form.html"
    fields = ["type", "size", "availability", "jobs"]
    success_url = reverse_lazy("equipment_list")

class EquipmentUpdateView(UpdateView):
    model = Equipment
    template_name = "equipment/equipment_form.html"
    fields = ["type", "size", "availability", "jobs"]
    success_url = reverse_lazy("equipment_list")

class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = "equipment/equipment_confirm_delete.html"
    success_url = reverse_lazy("equipment_list")

# CUSTOMER VIEWS
from .models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"

class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"

class CustomerCreateView(CreateView):
    model = Customer
    template_name = "customers/customer_form.html"
    fields = ["name", "email", "phone"]
    success_url = reverse_lazy("customer_list")

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "customers/customer_form.html"
    fields = ["name", "email", "phone"]
    success_url = reverse_lazy("customer_list")

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "customers/customer_confirm_delete.html"
    success_url = reverse_lazy("customer_list")

# DISPOSALDETAILS VIEWS
class DisposalCreateView(CreateView):
    model = DisposalDetails
    template_name = "jobs/disposal_form.html"
    fields = ["dump_site", "fee", "notes"]

    def form_valid(self, form):
        job = Job.objects.get(pk=self.kwargs["pk"])
        form.instance.job = job
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("job_detail", kwargs={"pk": self.kwargs["pk"]})


class DisposalUpdateView(UpdateView):
    model = DisposalDetails
    template_name = "jobs/disposal_form.html"
    fields = ["dump_site", "fee", "notes"]

    def get_success_url(self):
        return reverse_lazy("job_detail", kwargs={"pk": self.object.job.pk})


class DisposalDeleteView(DeleteView):
    model = DisposalDetails
    template_name = "jobs/disposal_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("job_detail", kwargs={"pk": self.object.job.pk})
    
def about_view(request):
    return render(request, "about.html")