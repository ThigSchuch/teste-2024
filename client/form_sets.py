from django import forms

from client.models import Client
from vehicle.forms import VehicleForm
from vehicle.models import Vehicle

ClientVehicleFormSet = forms.inlineformset_factory(
    Client, Vehicle, form=VehicleForm, extra=1, can_delete=True
)
