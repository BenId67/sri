from django.db import models
from apps.common.models import BaseModel
from apps.accounts.models import User
from apps.common.choices import AuditAction, AuditEntity

class AuditLog(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="audit_logs"
    )

    action = models.CharField(
        max_length=50,
        choices=AuditAction.choices
    )

    entity = models.CharField(
        max_length=50,
        choices=AuditEntity.choices
    )

    entity_id = models.CharField(
        max_length=100
    )

    description = models.TextField()

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "audit_logs"
        ordering = ["-created_at"]
        verbose_name = "Journal d'audit"
        verbose_name_plural = "Journaux d'audit"

    def __str__(self):
        return f"{self.get_action_display()} - {self.get_entity_display()}"