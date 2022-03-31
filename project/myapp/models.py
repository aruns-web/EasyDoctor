from django.db import models

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    dob = models.CharField(max_length=10)
    addr1 = models.CharField(max_length=500)
    addr2 = models.CharField(max_length=500)
    addr3 = models.CharField(max_length=500)
    pin = models.CharField(max_length=10)
    contact = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.fname

class doctor_master(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    d_descp = models.CharField(max_length=200)
    d_qualification = models.CharField(max_length=100)
    d_category = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=25)
    status = models.CharField(max_length=100)

class symptom_master(models.Model):
    symptom_name = models.CharField(max_length=100)

class disease_master(models.Model):
    disease_name = models.CharField(max_length=100)
    disease_descp = models.CharField(max_length=200)

class disease_symptom_map(models.Model):
    disease_id = models.IntegerField()
    symptom_id = models.IntegerField()

class disease_drug_map(models.Model):
    disease_id = models.IntegerField()
    drug_id = models.IntegerField()

class disease_treatment(models.Model):
    disease_id = models.IntegerField()
    treatment_plan = models.CharField(max_length=200)

class drug_master(models.Model):
    drug_name = models.CharField(max_length=100)
    drug_details = models.CharField(max_length=200)
    company_details = models.CharField(max_length=100)
    dosage_details = models.CharField(max_length=100)

class doctor_prescription(models.Model):
    doctor_id = models.IntegerField()
    user_id = models.IntegerField()
    prescription = models.CharField(max_length=200)
    dt = models.CharField(max_length=100)
    tm = models.CharField(max_length=100)
    status = models.CharField(max_length=10)

class user_doctor_query(models.Model):
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()
    query =  models.CharField(max_length=200)
    reply =  models.CharField(max_length=200)
    dt =  models.CharField(max_length=100)
    tm =  models.CharField(max_length=100)
    r_dt =  models.CharField(max_length=100)
    r_tm =  models.CharField(max_length=100)
    status =  models.CharField(max_length=10)

class user_bookings(models.Model):
    user_id = models.IntegerField()
    doctor_id = models.IntegerField()
    msg = models.CharField(max_length=200)
    dt = models.CharField(max_length=100)
    tm = models.CharField(max_length=100)
    status = models.CharField(max_length=10)






