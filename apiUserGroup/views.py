from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.mixins import UpdateModelMixin

from .serializer import UserSerializer


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveView(DestroyAPIView, UpdateModelMixin):
    queryset = User.objects
    serializer_class = UserSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)