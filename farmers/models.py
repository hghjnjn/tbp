# farmers/models.py
from django.db import models
from django.contrib.auth.models import User

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=50)
    price_today = models.DecimalField(max_digits=5, decimal_places=2)
    price_last_10_days = models.TextField()
