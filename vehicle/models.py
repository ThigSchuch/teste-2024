from django.db import models

from client.models import Client
from utils.models import BaseModel
from vehicle.validators import LicensePlateValidator


class Vehicle(BaseModel):
    license_plate = models.CharField(
        "license plate",
        max_length=8,
        unique=True,
        validators=[LicensePlateValidator()],
    )
    client = models.ForeignKey(
        Client, verbose_name="client", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "vehicle"
        verbose_name_plural = "vehicles"

    def __str__(self):
        return self.license_plate
