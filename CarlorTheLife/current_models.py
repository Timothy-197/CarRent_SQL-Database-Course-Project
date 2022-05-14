# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=400)
    category = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    color = models.CharField(max_length=15)
    capacity = models.DecimalField(max_digits=3, decimal_places=0)
    fuel_type = models.CharField(max_length=25)
    image = models.CharField(max_length=200, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    rent_price = models.FloatField()
    valid = models.TextField()  # This field type is a guess.
    owner = models.ForeignKey('Owner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'car'


class CarRentalDemand(models.Model):
    date = models.DateField(primary_key=True)
    hour = models.DecimalField(max_digits=2, decimal_places=0)
    demand = models.DecimalField(max_digits=5, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'car_rental_demand'
        unique_together = (('date', 'hour'),)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=8, decimal_places=0)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    cost = models.FloatField()
    order_date = models.DateField()
    begin_date = models.DateField()
    return_date = models.DateField()
    returned = models.TextField()  # This field type is a guess.
    car = models.ForeignKey(Car, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order'


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'owner'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review = models.CharField(max_length=500)
    rate = models.DecimalField(max_digits=1, decimal_places=0)
    date = models.DateField()
    renter_trips_taken = models.DecimalField(max_digits=4, decimal_places=0)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    car = models.ForeignKey(Car, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review'


class SysPurchaseNft(models.Model):
    id = models.BigAutoField(primary_key=True)
    nftname = models.CharField(db_column='NFTname', max_length=50)  # Field name made lowercase.
    description = models.CharField(max_length=200)
    img_url = models.CharField(max_length=100)
    ct_red = models.IntegerField(db_column='CT_red')  # Field name made lowercase.
    ct_green = models.IntegerField(db_column='CT_green')  # Field name made lowercase.
    ct_blue = models.IntegerField(db_column='CT_blue')  # Field name made lowercase.
    status = models.IntegerField()
    owner = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_Purchase_nft'


class SysReglogUserprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    usericon_url = models.CharField(db_column='userIcon_url', max_length=100)  # Field name made lowercase.
    userintro = models.CharField(db_column='userIntro', max_length=300)  # Field name made lowercase.
    userjob = models.CharField(db_column='userJob', max_length=30)  # Field name made lowercase.
    userhobby = models.CharField(db_column='userHobby', max_length=30)  # Field name made lowercase.
    usermobile = models.CharField(db_column='userMobile', max_length=15)  # Field name made lowercase.
    userlocation = models.CharField(db_column='userLocation', max_length=50)  # Field name made lowercase.
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sys_RegLog_userprofile'


class UserColortile(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    user_ct_red = models.IntegerField(db_column='user_CT_red')  # Field name made lowercase.
    user_ct_green = models.IntegerField(db_column='user_CT_green')  # Field name made lowercase.
    user_ct_blue = models.IntegerField(db_column='user_CT_blue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_colortile'


class UserGoal(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    goalname = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.IntegerField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()
    dead_line = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_goal'


class UserGoalFinished(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    goalname = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    finish_at = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_goal_finished'


class UserNft(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    nft_id = models.IntegerField()
    bought_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_nft'
