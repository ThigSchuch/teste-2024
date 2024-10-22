from django.core.validators import RegexValidator


class LicensePlateValidator(RegexValidator):
    regex = r"^\d{2}[A-Z]{2}\d{2}$|^\d{2}-\d{2}-[A-Z]{2}$"
    message = "License plate must be in format 00AA00 or 00-00-AA"
