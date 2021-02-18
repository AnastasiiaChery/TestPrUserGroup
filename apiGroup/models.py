from django.db import models
from django.contrib.auth.models import Group, User


class DescriptionModel(models.Model):
    properties = models.CharField(max_length=50)

    class Meta:
        db_table = 'properties'

    def __str__(self):
        return self.properties


class GroupDescription(models.Model):
    group = models.ManyToManyField(Group)
    description = models.ManyToManyField(DescriptionModel)

    class Meta:
        db_table = 'group_descriptions'


class UserGroups(models.Model):
    group = models.ManyToManyField(Group)
    user = models.ManyToManyField(User)

    class Meta:
        db_table = 'group_user'
