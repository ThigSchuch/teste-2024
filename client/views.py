from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, TemplateView

from client.models import Client


class ClientHomeView(TemplateView):
    template_name = "client/home.html"


class ClientListView(ListView):
    model = Client
    template_name = "client/client/list.html"


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "client/client/delete.html"
    success_url = reverse_lazy("client:list_client")
