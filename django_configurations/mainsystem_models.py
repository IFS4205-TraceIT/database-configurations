# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Buildingaccess(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    building = models.ForeignKey('Buildings', models.DO_NOTHING)
    access_timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'buildingaccess'
        unique_together = (('user', 'building', 'access_timestamp'),)


class Buildings(models.Model):
    name = models.TextField()
    location = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'buildings'


class Closecontacts(models.Model):
    infected_user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    contacted_user = models.ForeignKey('Users', models.DO_NOTHING)
    contact_timestamp = models.DateTimeField()
    rssi = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'closecontacts'
        unique_together = (('infected_user', 'contacted_user', 'contact_timestamp'),)


class Contacttracers(models.Model):
    uuid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'contacttracers'


class Infectionhistory(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    recorded_timestamp = models.DateTimeField()
    has_uploaded = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infectionhistory'
        unique_together = (('user', 'recorded_timestamp'),)


class Notifications(models.Model):
    due_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    tracer = models.ForeignKey(Contacttracers, models.DO_NOTHING, blank=True, null=True)
    infected_user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class Users(models.Model):
    nric = models.TextField(unique=True)
    name = models.TextField()
    dob = models.DateField()
    email = models.TextField(blank=True, null=True)
    phone = models.IntegerField()
    gender = models.CharField(max_length=1)
    address = models.TextField()
    zip_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Vaccinationhistory(models.Model):
    user = models.OneToOneField(Users, models.DO_NOTHING, primary_key=True)
    vaccination = models.ForeignKey('Vaccinationtypes', models.DO_NOTHING)
    date_taken = models.DateField()

    class Meta:
        managed = False
        db_table = 'vaccinationhistory'
        unique_together = (('user', 'vaccination', 'date_taken'),)


class Vaccinationtypes(models.Model):
    name = models.TextField()
    start_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'vaccinationtypes'
