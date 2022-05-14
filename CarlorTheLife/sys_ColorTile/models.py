from re import S
from django.db import models
from datetime import datetime,timedelta

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    cost = models.FloatField()
    order_date = models.DateField()
    begin_date = models.DateField()
    return_date = models.DateField()
    returned = models.IntegerField()  # This field type is a guess.
    car= models.ForeignKey('sys_Purchase.Car', models.DO_NOTHING)
    customer = models.ForeignKey('sys_RegLog.Customer', models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'order'