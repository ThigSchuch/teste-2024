from django.urls import path

from client.views import (
    ClientCreateView,
    ClientDeleteView,
    ClientListView,
    ClientUpdateView,
)

app_name = "client"

urlpatterns = [
    path("list/", ClientListView.as_view(), name="list_client"),
    path("create/", ClientCreateView.as_view(), name="create_client"),
    path("update/<int:pk>/", ClientUpdateView.as_view(), name="update_client"),
    path("delete/<int:pk>/", ClientDeleteView.as_view(), name="delete_client"),
]
