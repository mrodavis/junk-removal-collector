from django.contrib import admin
from .models import Customer, Job, Hauler, Equipment, DisposalDetails

admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(Hauler)
admin.site.register(Equipment)
admin.site.register(DisposalDetails)
