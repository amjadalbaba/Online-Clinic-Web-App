from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(DoctorSchedule)
admin.site.register(Appointments)
admin.site.register(Consultation)
admin.site.register(Speciality)
admin.site.register(DoctorSpeciality)
admin.site.register(Drugs)
admin.site.register(doctorNotice)
admin.site.register(patientNotice)