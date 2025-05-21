from django.db import models


class XAccount(models.Model):
    id = models.BigIntegerField()
    handle = models.CharField(max_length=50) # Reduce limit

    class Meta:
        managed = False # Avoid messing with the existing Account table
        db_table = 'accounts'


class XUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=50)

    class Meta:
        managed = False # Avoid messing with the existing User table
        db_table = 'users'