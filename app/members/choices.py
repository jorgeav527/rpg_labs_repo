from django.db import models

# |value|human-readable name, or label|


class Roles(models.TextChoices):
    NONE = None, 'Escoje el Rol'
    CLIENT = 'CLI', 'Cliente'
    ADMIN = 'ADM', 'Admin'


class Professions(models.TextChoices):
    NONE = None, 'Escoje la Profesión'
    ENGINEER = 'ING', 'Ingeníero'
    TECHNICIAN = 'TEC', 'Técnico'
    MISTER_MISSES = 'SR_a', 'Señor(a)'
