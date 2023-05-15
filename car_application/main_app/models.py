from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.



class Upgrade(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    cost = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("upgrade_detail", kwargs={"pk": self.pk})
    


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    upgrade = models.ManyToManyField(Upgrade)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} {self.model}'
    
    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.id})
    


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    parts = models.CharField(max_length=250)
    cost = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name