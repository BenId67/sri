from django.db import models
from apps.common.models import BaseModel

class Checkpoint(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(
        unique=True, default=3
    )

    is_entry = models.BooleanField(
        default=False
    )

    is_exit = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "checkpoints"
        ordering = ["order"]

    def __str__(self):
        return self.name
    
class Validation(BaseModel):
    checkpoint = models.ForeignKey(Checkpoint, on_delete=models.CASCADE, related_name="validations")
    visit = models.ForeignKey('visitors.Visitor', on_delete=models.CASCADE, related_name="validations")
    validated_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="validations")
    status = models.CharField(max_length=50, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    validated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "Validation"
        ordering = ["checkpoint", "visit", "validated_at"]
    def __str__(self):
        return f"{self.status} {self.comments}"
