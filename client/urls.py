from django.urls import path

from client.views import ClientListView

app_name = "client"

urlpatterns = [
    path("list/", ClientListView.as_view(), name="list_client"),
]
