from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'
