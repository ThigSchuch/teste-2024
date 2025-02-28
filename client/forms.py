from django import forms

from client.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ["is_active"]
