from django.db import models


class TypeService(models.TextChoices):
    TEST = "TEST", "Ensayo"
    SOIL_MECHANICS_STUDY = "SOIL_MECHANICS_STUDY", "Estudio de Mecánica de Suelos"
    GEOTECHNICS_STYDY = "GEOTECHNICS_STYDY", "Estudio de Geotécnico"
