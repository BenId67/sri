from django.db import models

from common.models import BaseModel
from common.choices import DocumentType, Gender
from apps.validation.models import Checkpoint

class Workflow(BaseModel):
    name = models.CharField(max_length=255)
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
    checkpoint = models.ForeignKey(Checkpoint, on_delete=models.CASCADE, related_name="workflow_steps")
    order = models.PositiveIntegerField()
    is_required = models.BooleanField(default=True)

    class Meta:
        db_table = "WorkflowStep"
        ordering = ["order"]
        unique_together = ("workflow", "order")
    def __str__(self):
        return f"{self.workflow.name} - {self.checkpoint} (Order: {self.order})"
    
