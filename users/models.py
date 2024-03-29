from django.db import models

from core.models import TimeStampModel

class User(TimeStampModel):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.CharField(max_length=100, unique=True)
    password   = models.CharField(max_length=200)

    class Meta:
        db_table = 'users'

