from django.urls import path

from client.views import ClientDeleteView, ClientListView

app_name = "client"

urlpatterns = [
    path("list/", ClientListView.as_view(), name="list_client"),
    path("delete/<int:pk>/", ClientDeleteView.as_view(), name="delete_client"),
]
