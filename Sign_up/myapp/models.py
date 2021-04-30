from django.db import models


# Create your models here.
class register(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phoneNo = models.CharField(max_length=13)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.firstName + " " + self.lastName