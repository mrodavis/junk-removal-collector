from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Job, Hauler, Equipment, DisposalDetails, Customer


# AUTH
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# =====================
# JOB VIEWS
# =====================
class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = "jobs/job_list.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return Job.objects.filter(owner=self.request.user)


class JobDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Job
    template_name = "jobs/job_detail.html"

    def test_func(self):
        return self.get_object().owner == self.request.user


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = "jobs/job_form.html"
    fields = ["customer", "description", "address", "date", "status", "haulers"]
    success_url = reverse_lazy("job_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user

        form.fields["customer"].queryset = Customer.objects.filter(owner=user)
        form.fields["haulers"].queryset = Hauler.objects.filter(owner=user)
        # form.fields["equipment"].queryset = Equipment.objects.filter(owner=user)
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        customer_id = self.request.GET.get("customer")
        if customer_id:
            initial["customer"] = customer_id
        return initial


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    template_name = "jobs/job_form.html"
    fields = ["customer", "description", "address", "date", "status", "haulers"]
    success_url = reverse_lazy("job_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user

        form.fields["customer"].queryset = Customer.objects.filter(owner=user)
        form.fields["haulers"].queryset = Hauler.objects.filter(owner=user)
        # form.fields["equipment"].queryset = Equipment.objects.filter(owner=user)
        return form
    
    def test_func(self):
        return self.get_object().owner == self.request.user


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    template_name = "jobs/job_confirm_delete.html"
    success_url = reverse_lazy("job_list")

    def test_func(self):
        return self.get_object().owner == self.request.user


# =====================
# HAULER VIEWS
# =====================
class HaulerListView(LoginRequiredMixin, ListView):
    model = Hauler
    template_name = "haulers/hauler_list.html"
    context_object_name = "haulers"

    def get_queryset(self):
        return Hauler.objects.filter(owner=self.request.user)


class HaulerDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Hauler
    template_name = "haulers/hauler_detail.html"

    def test_func(self):
        return self.get_object().owner == self.request.user


class HaulerCreateView(LoginRequiredMixin, CreateView):
    model = Hauler
    template_name = "haulers/hauler_form.html"
    fields = ["name", "phone", "email", "truck_type", "availability"]
    success_url = reverse_lazy("hauler_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class HaulerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Hauler
    template_name = "haulers/hauler_form.html"
    fields = ["name", "phone", "email", "truck_type", "availability"]
    success_url = reverse_lazy("hauler_list")

    def test_func(self):
        return self.get_object().owner == self.request.user


class HaulerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Hauler
    template_name = "haulers/hauler_confirm_delete.html"
    success_url = reverse_lazy("hauler_list")

    def test_func(self):
        return self.get_object().owner == self.request.user


# =====================
# EQUIPMENT VIEWS
# =====================
class EquipmentListView(LoginRequiredMixin, ListView):
    model = Equipment
    template_name = "equipment/equipment_list.html"
    context_object_name = "equipment"

    def get_queryset(self):
        return Equipment.objects.filter(owner=self.request.user)


class EquipmentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Equipment
    template_name = "equipment/equipment_detail.html"

    def test_func(self):
        return self.get_object().owner == self.request.user


class EquipmentCreateView(LoginRequiredMixin, CreateView):
    model = Equipment
    template_name = "equipment/equipment_form.html"
    fields = ["type", "size", "availability", "jobs"]
    success_url = reverse_lazy("equipment_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user
        form.fields["jobs"].queryset = Job.objects.filter(owner=user)
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class EquipmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Equipment
    template_name = "equipment/equipment_form.html"
    fields = ["type", "size", "availability", "jobs"]
    success_url = reverse_lazy("equipment_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user
        form.fields["jobs"].queryset = Job.objects.filter(owner=user)
        return form

    def test_func(self):
        return self.get_object().owner == self.request.user


class EquipmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Equipment
    template_name = "equipment/equipment_confirm_delete.html"
    success_url = reverse_lazy("equipment_list")

    def test_func(self):
        return self.get_object().owner == self.request.user


# =====================
# CUSTOMER VIEWS
# =====================
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"

    def get_queryset(self):
        return Customer.objects.filter(owner=self.request.user)


class CustomerDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"

    def test_func(self):
        return self.get_object().owner == self.request.user


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = "customers/customer_form.html"
    fields = ["name", "email", "phone", "address"]
    success_url = reverse_lazy("customer_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CustomerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Customer
    template_name = "customers/customer_form.html"
    fields = ["name", "email", "phone", "address"]
    success_url = reverse_lazy("customer_list")

    def test_func(self):
        return self.get_object().owner == self.request.user


class CustomerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Customer
    template_name = "customers/customer_confirm_delete.html"
    success_url = reverse_lazy("customer_list")

    def test_func(self):
        return self.get_object().owner == self.request.user


# =====================
# DISPOSALDETAILS VIEWS
# =====================
class DisposalCreateView(LoginRequiredMixin, CreateView):
    model = DisposalDetails
    template_name = "jobs/disposal_form.html"
    fields = ["dump_site", "fee", "notes"]

    def form_valid(self, form):
        job = Job.objects.get(pk=self.kwargs["pk"])
        form.instance.job = job
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("job_detail", kwargs={"pk": self.kwargs["pk"]})


class DisposalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DisposalDetails
    template_name = "jobs/disposal_form.html"
    fields = ["dump_site", "fee", "notes"]

    def test_func(self):
        return self.get_object().owner == self.request.user

    def get_success_url(self):
        return reverse_lazy("job_detail", kwargs={"pk": self.object.job.pk})


class DisposalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DisposalDetails
    template_name = "jobs/disposal_confirm_delete.html"

    def test_func(self):
        return self.get_object().owner == self.request.user

    def get_success_url(self):
        return reverse_lazy("job_detail", kwargs={"pk": self.object.job.pk})


# ABOUT PAGE
def about_view(request):
    return render(request, "about.html")
