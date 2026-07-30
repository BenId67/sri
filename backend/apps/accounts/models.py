from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.common.models import BaseModel


class Role(BaseModel):
    name = models.CharField(max_length=100,
        unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Rôle"
        verbose_name_plural = "Rôles"
    def __str__(self):
        return self.name

class User(AbstractUser, BaseModel):
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=False, blank=True, related_name="users")
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)



    class Meta:
        db_table = "users"
        ordering = ["last_name", "first_name"]
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"