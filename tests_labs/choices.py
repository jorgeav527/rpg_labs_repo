from django.db import models


class Matrices(models.TextChoices):
    NONE = None, 'Escoje la Matriz de tipo de ensayos'
    MS = 'MS', 'Ensayos de Mecánica de Suelos'
    VAR = 'VAR', 'Escavación - Resanes - Transportes - Varios'
    EMS = 'EMS', 'Estudio de Mecánica de Suelos para Cimentaciones, Canales Tuberías y Pavimentos'
    AG = 'AG', 'Ensayos para Agregados y Caracterización'
    MEZCLA = 'MEZCLA', 'Diseños de Mezclas'
    CONC = 'CONC', 'Ensayos para Concreto de Cemento Portland'
    PAV = 'PAV', 'Ensayos para Pavimentos'


class Labs(models.TextChoices):
    NONE = None, 'Escoja el Laboratorio'
    RPG = 'RPG', 'Grupo RPG SAC'
    DINATEST = 'DINATEST', 'Grupo DINATEST SAC'
    TDM = 'TDM', 'Grupo TDM SAC'


class Unit(models.TextChoices):
    NONE = None, 'Escoja la unidad'
    UND = 'UND', 'Und.'
    NOCHE = 'NOCHE', 'noche'
    DIA = 'DIA', 'día'
    POBETA = 'PROBETA', 'probeta'
