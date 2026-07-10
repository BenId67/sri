from django.db import models
from common.models import BaseModel

class Checkpoint(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "Checkpoint"
        ordering = ["name"]
    def __str__(self):
        return f"{self.name} {self.type} {self.description}"
    
class Validation(BaseModel):
    checkpoint = models.ForeignKey(Checkpoint, on_delete=models.CASCADE, related_name="validations")
    visit = models.ForeignKey('visitors.Visitor', on_delete=models.CASCADE, related_name="validations")
    validated_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="validations")
    status = models.CharField(max_length=50, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    validated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "Validation"
        ordering = ["name"]
    def __str__(self):
        return f"{self.name} {self.description}"
