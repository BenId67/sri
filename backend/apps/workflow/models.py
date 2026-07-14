from django.db import models

from apps.common.models import BaseModel
from apps.common.choices import DocumentType, Gender
from apps.validation.models import Checkpoint

class Workflow(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "Workflow"
        ordering = ["name"]
    def __str__(self):
        return self.name

class WorkflowStep(BaseModel):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name="steps")

    checkpoint = models.ForeignKey(Checkpoint, on_delete=models.PROTECT, related_name="workflow_steps")

    step_order = models.PositiveIntegerField()

    is_required = models.BooleanField(default=True)

    class Meta:
        db_table = "workflow_steps"
        ordering = ["step_order"]

    def __str__(self):
        return f"{self.step_order} - {self.checkpoint.name}"
    
