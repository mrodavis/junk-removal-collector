from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="jobs")
    description = models.TextField()
    address = models.CharField(max_length=255)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    haulers = models.ManyToManyField("Hauler", related_name="jobs", blank=True)

    def __str__(self):
        return f"{self.description} ({self.status})"


class Hauler(models.Model):
    name = models.CharField(max_length=100)
    truck_type = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Equipment(models.Model):
    type = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    jobs = models.ManyToManyField(Job, related_name="equipment", blank=True)

    def __str__(self):
        return f"{self.type} ({self.size})"


class DisposalDetails(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name="disposal_details")
    dump_site = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=8, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job.description} disposal"
