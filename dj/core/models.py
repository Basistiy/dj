from django.db import models

# Create your models here.

class Contacts(models.Model):
    fName = models.CharField(max_length=60)
    lName = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    imageUrl = models.CharField(max_length=60)

    def __str__(self):
        return self.title
