from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group
from .models import GroupDescription, UserGroups

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

    def create(self, validated_data):
        group = Group(**validated_data)
        group.save()
        return group


class GroupDescriptionSerializer(ModelSerializer):
    class Meta:
        model = GroupDescription
        fields = '__all__'

class UserGroupSerializer(ModelSerializer):
    class Meta:
        model = UserGroups
        fields = '__all__'

