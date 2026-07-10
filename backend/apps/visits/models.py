from django.db import models
from backend.apps.common.models import BaseModel
# Create your models here.

class Visit(BaseModel):
    visitor = models.ForeignKey('visitors.Visitor', on_delete=models.CASCADE)
    workflow = models.ForeignKey('workflow.Workflow', on_delete=models.CASCADE)
    visit_date = models.DateTimeField()
    purpose = models.TextField()
    host_name = models.CharField(max_length=255)
    host_department = models.CharField(max_length=255)
    host_email = models.EmailField()
    host_phone = models.CharField(max_length=20)

    class Meta:
        db_table = "Visit"
        ordering = ["-visit_date"]

    def __str__(self):
        return f"Visit by {self.visitor} on {self.visit_date}"