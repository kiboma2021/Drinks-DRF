from django.db import models

# Create your models here.

class soft_drink(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=500)

    def __str__(self):
        return self.name

class alcohol(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=500)

    def __str__(self):
        return self.name

class soda(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=500)

    def __str__(self):
        return self.name