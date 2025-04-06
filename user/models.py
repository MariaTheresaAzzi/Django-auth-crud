from django.db import models

class Doctor(models.Model):
    # doctor_id = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Patient(models.Model):
    # patient_id = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    date_of_birth = models.DateField()
    medical_file = models.FileField(upload_to='medical_files/', blank=True, null=True)
    image = models.ImageField(upload_to='patient_images/', blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name="patients")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
