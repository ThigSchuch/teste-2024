from django.db import models

from utils.models import BaseModel


class Client(BaseModel):
    email = models.EmailField("email", unique=True)

    class Meta:
        verbose_name = "client"
        verbose_name_plural = "clients"

    def __str__(self):
        return self.email
