# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class XAccount(models.Model):
    handle = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class XUser(models.Model):
    account = models.ForeignKey(XAccount, models.DO_NOTHING, blank=True, null=True)
    handle = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    following_count = models.IntegerField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    featured_url = models.CharField(blank=True, null=True)
    follower = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('handle', 'created_at'),)