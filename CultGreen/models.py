from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=55, null=True)
    last_name = models.CharField(max_length=55, null=True)
    email = models.EmailField(max_length=55, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

class Plant(models.Model):
    plant_name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='plant_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plant_name

class Watering(models.Model):
    user_plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    liters = models.IntegerField(null=True, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_plant)

class Sunlight(models.Model):
    user_plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    duration_hours = models.PositiveIntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_plant)