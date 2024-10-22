from django.views.generic import ListView, TemplateView

from client.models import Client


class ClientHomeView(TemplateView):
    template_name = "client/home.html"


class ClientListView(ListView):
    model = Client
    template_name = "client/client/list.html"
