from django.urls import path

from .views import UserListCreateView, UserRetrieveView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_crate'),
    path('/<int:id>', UserRetrieveView.as_view(), name="office_retrieve"),
]