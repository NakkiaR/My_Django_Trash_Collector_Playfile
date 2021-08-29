from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField
from django import utils
import django.utils.timezone 

# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    street_address = models.CharField(blank=True, max_length=50)
    zip_code = models.CharField('customer.Zip Code', max_length=5)
    amount = models.IntegerField()
    weekly_pickup = models.CharField(default=True, null=True, max_length=50)
    one_time_pickup = models.DateField(default=django.utils.timezone.now, null=True)
    suspend_start = models.DateField(default=django.utils.timezone.now, null=True)
    suspend_end = models.DateField(default=django.utils.timezone.now, null=True)

    def __str__(self): 
        return self.name
    
    
 
 