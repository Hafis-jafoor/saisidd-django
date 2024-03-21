from django.db import models

# Create your models here.
class contacts(models.Model):
    contact_name  = models.CharField(max_length=255)
    contact_email = models.EmailField(unique = True)
    contact_phone = models.CharField(max_length=10)
    contact_subject = models.CharField(max_length=100)
    contact_message = models.TextField()
