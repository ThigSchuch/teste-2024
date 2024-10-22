from abc import ABC, abstractmethod

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from client.form_sets import ClientVehicleFormSet
from client.forms import ClientForm
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


class ClientVehicleInline(ABC):
    form_class = ClientForm
    model = Client
    template_name = "client/client/create_update.html"

    @abstractmethod
    def get_formsets(self):
        pass

    def get_success_url(self):
        return reverse_lazy("client:list_client")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formsets"] = self.get_formsets()
        return context

    def form_valid(self, form):
        formsets = self.get_formsets()

        if not all((formset.is_valid() for formset in formsets.values())):
            return self.render_to_response(self.get_context_data(form=form, **formsets))

        self.object = form.save()

        for formset in formsets.values():
            form_formset = formset.save(commit=False)

            for obj in formset.deleted_objects:
                obj.delete()

            for obj in form_formset:
                obj.client = self.object
                obj.save()

        return super().form_valid(form)


class ClientCreateView(ClientVehicleInline, CreateView):
    def get_formsets(self):
        if self.request.POST:
            return {"vehicles": ClientVehicleFormSet(self.request.POST or None)}

        return {"vehicles": ClientVehicleFormSet()}


class ClientUpdateView(ClientVehicleInline, UpdateView):
    def get_formsets(self):
        return {
            "vehicles": ClientVehicleFormSet(
                self.request.POST or None, instance=self.object
            )
        }
