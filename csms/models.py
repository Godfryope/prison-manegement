from django.db import models


# Model for Facilities
class Facility(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    # Add other facility-related fields here

    def __str__(self):
        return self.name
    
class Inmate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    inmate_id = models.CharField(max_length=10, unique=True)
    facility = models.ForeignKey('Facility', on_delete=models.CASCADE)
    
    # Add more inmate-related fields
    gender = models.CharField(max_length=10)
    admission_date = models.DateField()
    release_date = models.DateField(blank=True, null=True)
    # Add other inmate-related fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CorrectionalOfficer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    badge_number = models.CharField(max_length=10, unique=True)
    
    # Add more correctional officer-related fields
    rank = models.CharField(max_length=20)
    hire_date = models.DateField()
    # Add other correctional officer-related fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
