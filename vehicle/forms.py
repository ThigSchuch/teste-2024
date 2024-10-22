from django import forms

from vehicle.models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ["is_active"]
