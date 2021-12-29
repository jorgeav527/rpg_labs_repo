from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from companies.models import Company
from core.utils import *

from .choices import Roles, Professions


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('usuarios deben tener una dirección email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        user = self._create_user(email, password, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', Roles.ADMIN)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super usuario debe ser staff is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Debe ser super usuario is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    username = None
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    dni = models.BigIntegerField(unique=True, null=True, default=None)
    role = models.CharField(
        max_length=4, choices=Roles.choices, default=Roles.NONE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")
        ordering = ["-date_joined"]

    def __str__(self):
        return f'DNI: {self.dni}, Email: {self.email}'

    def get_role(self):
        role_name = None
        if self.role == Roles.ADMIN:
            role_name = 'Administrador'
        return role_name


# class ClientProfile(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='related client profile')
#     company = models.ForeignKey(
#         Company, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='the related company')
#     profession = models.CharField(verbose_name='profession',
#                                   max_length=4, choices=Professions.choices, default=Professions.ENGINEER)
#     cell_phone = models.PositiveBigIntegerField(
#         verbose_name='cell phone', blank=True, null=True)
#     created = models.DateTimeField(
#         verbose_name='created at', auto_now_add=True)
#     updated = models.DateTimeField(verbose_name='updated at', auto_now=True)

#     def __str__(self):
#         return f'{self.profession} {self.user.first_name} {self.user.last_name}'


class AdminProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='related admin profile')
    profession = models.CharField(
        max_length=4, choices=Professions.choices, default=Professions.NONE)
    cell_phone = models.PositiveBigIntegerField(blank=True, null=True)
    created = models.DateTimeField(
        verbose_name='created at', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated at', auto_now=True)

    def __str__(self):
        return f'{self.profession} {self.user.first_name} {self.user.last_name}'

# https://docs.djangoproject.com/en/3.2/ref/models/fields/#primary-key
# https://tech.serhatteker.com/post/2020-01/email-as-username-django/
