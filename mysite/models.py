from django.contrib.auth.models import User
from django.db import models


class MyModel(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.phone


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()


class Registration(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    membership_type = models.CharField(max_length=50)
