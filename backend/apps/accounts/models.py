from django.db import models
from django.contrib.auth.models import AbstractUser

from common.models import BaseModel


class Role(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    

    class Meta:
        db_table = "Role"
        ordering = ["name"]
    def __str__(self):
        return self.name

class User(AbstractUser, BaseModel):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    