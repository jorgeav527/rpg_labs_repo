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
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email es requerido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super usuario debe ser staff is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Debe ser super usuario is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    dni = models.BigIntegerField(verbose_name='DNI', null=True, default=None)
    role = models.CharField(verbose_name='roles', max_length=3,
                            choices=Roles.choices, default=Roles.CLIENT)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dni']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.dni} email: {self.email}'


class ClientProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='related client profile')
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='the related company')
    profession = models.CharField(verbose_name='profession',
                                  max_length=4, choices=Professions.choices, default=Professions.ENGINEER)
    cell_phone = models.PositiveBigIntegerField(
        verbose_name='cell phone', blank=True, null=True)
    created = models.DateTimeField(
        verbose_name='created at', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated at', auto_now=True)

    def __str__(self):
        return f'{self.profession} {self.user.first_name} {self.user.last_name}'


class AdminProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='related admin profile')
    profession = models.CharField(verbose_name='profession',
                                  max_length=4, choices=Professions.choices, default=Professions.TECHNICIAN)
    cell_phone = models.PositiveBigIntegerField(
        verbose_name='cell phone', blank=True, null=True)
    created = models.DateTimeField(
        verbose_name='created at', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated at', auto_now=True)

    def __str__(self):
        return f'{self.profession} {self.user.first_name} {self.user.last_name}'

# https://docs.djangoproject.com/en/3.2/ref/models/fields/#primary-key
# https://tech.serhatteker.com/post/2020-01/email-as-username-django/
