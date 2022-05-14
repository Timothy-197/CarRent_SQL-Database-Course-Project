from distutils.command.upload import upload
from django.db import models

from django.utils.html import format_html

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=400)
    category = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    color = models.CharField(max_length=15)
    capacity = models.DecimalField(max_digits=3, decimal_places=0)
    fuel_type = models.CharField(max_length=25)
    image = models.ImageField(upload_to="Car/")
    rate = models.FloatField(blank=True, null=True)
    rent_price = models.FloatField()
    valid = models.IntegerField()  # This field type is a guess.
    returned = models.IntegerField()  # This field type is a guess.
    owner = models.ForeignKey('sys_RegLog.Owner', models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'car'

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='Car/')

    class Meta:
        #managed = False
        db_table = 'image'   