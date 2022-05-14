from django.db import models
from django.utils.html import format_html
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

from django.contrib.auth.models import User
from zmq import NULL

class UserProfile(models.Model):
    #REQUIRED_FIELDS = ('user',)
    #identifier = models.CharField(max_length=40, unique=True)
    #USERNAME_FIELD = 'identifier'
    #is_anonymous=True
    #is_authenticated=True

    user   = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, unique=True)
    userIcon_url = models.ImageField(upload_to = 'UserIcon/',default = "UserIcon/default.png")
    userIntro = models.CharField(max_length=300, default='He is BUSY in doing CSC4001 project! Nothing Left!')
    userJob = models.CharField(max_length=30, default='Programming')
    userHobby = models.CharField(max_length=30, default='Running')
    userMobile= models.CharField(max_length=15, default='15857358070')
    user_is_customer = models.IntegerField(default = 1)
    userLocation= models.CharField(max_length=50, default='The Chinise University of Hong Kong, Shenzhen')



    class Meta:
        verbose_name = 'UserProfile'  
        verbose_name_plural = 'UserProfile Management'

    def userIcon(self):
        if self.userIcon_url:
            return format_html('<img src="/media/{}" width="80px"/>', self.userIcon_url)
        else:
            return format_html('<img src="/media/blank.jpg" width="80px"/>', self.userIcon_url)
    
    def userFullname(self):
        return self.user.first_name + self.user.last_name
  
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default = NULL)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)

    class Meta:
        #managed = False
        db_table = 'owner'

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default = NULL)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=8, decimal_places=0)
    password = models.CharField(max_length=30)

    class Meta:
        #managed = False
        db_table = 'customer'

