from django.contrib import admin

# Register your models here.


from .models import DescriptionModel, GroupDescription, UserGroups

admin.site.register(DescriptionModel)
admin.site.register(GroupDescription)
admin.site.register(UserGroups)