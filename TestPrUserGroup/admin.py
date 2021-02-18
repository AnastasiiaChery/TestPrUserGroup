from django.contrib import admin

# Register your models here.


from apiGroup.models import DescriptionModel, GroupDescription

admin.site.register(DescriptionModel)
admin.site.register(GroupDescription)