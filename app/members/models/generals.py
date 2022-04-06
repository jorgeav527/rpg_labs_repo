from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from core.utils import *

from members.choices import Roles, Professions


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("usuarios deben tener una dirección email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        user = self._create_user(email, password, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", Roles.ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Super usuario debe ser staff is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Debe ser super usuario is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    dni = models.BigIntegerField(
        unique=True,
        blank=True,
        null=True,
        default=None,
    )
    role = models.CharField(
        max_length=4,
        choices=Roles.choices,
        default=Roles.NONE,
    )
    profession = models.CharField(
        max_length=4,
        choices=Professions.choices,
        default=Professions.NONE,
    )
    cell_phone = models.PositiveBigIntegerField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["-date_joined"]

    def __str__(self):
        return f"{self.role}, Email: {self.email}"

    # def get_role(self):
    #     role_name = None
    #     if self.role == Roles.ADMIN:
    #         role_name = 'Administrador'
    #     return role_name
