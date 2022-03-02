from django.db import models


class TypeCompany(models.TextChoices):
    INTER = "INTER", "Interno"
    STATE_ENTITY = "STATE_ENTITY", "Entidad del Estado"
    ENTERPRICE = "ENTERPRICE", "Empresa"
    NATURAL_PERSON = "NATURAL_PERSON", "Persona Natural"
