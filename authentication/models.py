from django.db import models

class Train(models.Model):
    train_name = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    total_seats = models.IntegerField()  # New field for total seats available
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.train_name

from django.db import models
from django.contrib.auth.models import User  # Assuming user authentication is handled by Django's User model

class Train(models.Model):
    train_name = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    total_seats = models.IntegerField()  # Total seats available
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.train_name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who booked the seat
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    booked_seats = models.IntegerField()

    def __str__(self):
        return f"Booking by {self.user.username} on {self.train.train_name}"






