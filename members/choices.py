from django.db import models


class Roles(models.TextChoices):
    CLIENT = 'CLI', 'Cliente'
    ADMIN = 'ADM', 'Admin'


class Professions(models.TextChoices):
    ENGINEER = 'ING', 'Ingeníero'
    TECHNICIAN = 'TEC', 'Técnico'
    MISTER_MISSES = 'SR_a', 'Señor(a)'
