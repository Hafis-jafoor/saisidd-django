from django.db import models

# Create your models here.
class contacts(models.Model):
    contact_name  = models.CharField(max_length=255)
    contact_email = models.EmailField(unique = True)
    contact_phone = models.CharField(max_length=10)
    contact_subject = models.CharField(max_length=100)
    contact_message = models.TextField()

class admissions(models.Model):
    admission_name  = models.CharField(max_length=255)
    admission_number = models.CharField(max_length=10)
    admission_email = models.EmailField(unique = True)
    admission_state = models.CharField(max_length=50)
    admission_city = models.CharField(max_length=50)
    admission_pincode = models.CharField(max_length=6)
    admission_department = models.CharField(max_length=50)