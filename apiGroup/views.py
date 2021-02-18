from django.contrib.auth.models import Group, User
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.mixins import UpdateModelMixin

from .serializer import GroupSerializer, GroupDescriptionSerializer,  UserGroupSerializer
from .models import GroupDescription, UserGroups

#Таблица группы
class GroupListCreateView(ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupRetrieveView(DestroyAPIView, UpdateModelMixin):
    queryset = Group.objects
    serializer_class = GroupSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

#Таблица свойства группы

class AddProperties(ListCreateAPIView):
    serializer_class = GroupDescriptionSerializer
    queryset = GroupDescription.objects.all()


class GroupPropertiesRetrieveView(DestroyAPIView, UpdateModelMixin):
    queryset = GroupDescription.objects
    serializer_class = GroupDescriptionSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

#Таблица юзеры для группы

class AddUserInGroup(ListCreateAPIView):
    serializer_class = UserGroupSerializer
    queryset = UserGroups.objects.all()


class GroupUserRetrieveView(DestroyAPIView, UpdateModelMixin):
    queryset = UserGroups.objects
    serializer_class = UserGroupSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)