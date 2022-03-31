from django.contrib import admin

# Register your models here.
from .models import user_login, user_details, doctor_master, symptom_master, disease_master, disease_symptom_map, disease_drug_map, disease_treatment, drug_master, doctor_prescription, user_doctor_query, user_bookings



admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(doctor_master)
admin.site.register(symptom_master)
admin.site.register(disease_master)
admin.site.register(disease_symptom_map)
admin.site.register(disease_drug_map)
admin.site.register(disease_treatment)
admin.site.register(drug_master)
admin.site.register(doctor_prescription)
admin.site.register(user_doctor_query)
admin.site.register(user_bookings)


