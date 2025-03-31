from django.db import models

# Create your models here.

class Doctor(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.name  # Show doctor's name in admin panel & queries


class Patient(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.TextField()
    date_of_birth = models.DateField()
    medical_file = models.FileField(upload_to='medical_files/', blank=True, null=True)
    image = models.ImageField(upload_to='patient_images/', blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name="patients")

    def __str__(self):
        return self.name  # Show patient's name in admin panel & queries
