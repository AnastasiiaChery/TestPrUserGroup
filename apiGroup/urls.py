from django.urls import path

from .views import GroupListCreateView, GroupRetrieveView, AddProperties, GroupPropertiesRetrieveView, AddUserInGroup, GroupUserRetrieveView

urlpatterns = [
    path('', GroupListCreateView.as_view(), name='group_list_crate'),
    path('/properties', AddProperties.as_view(), name='properties_list_crate'),
    path('/<int:id>', GroupRetrieveView.as_view(), name="group_retrieve"),
    path('/properties/<int:id>', GroupPropertiesRetrieveView.as_view(), name='group_properties_retrieve'),
    path('/useringroup', AddUserInGroup.as_view(), name="user_group_list_create"),
    path('/useringroup/<int:id>', GroupUserRetrieveView.as_view(), name='user_group_retrieve')
]