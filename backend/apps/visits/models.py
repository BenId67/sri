from django.db import models
from apps.common.models import BaseModel
from apps.visitors.models import Visitor
from apps.workflow.models import Workflow
from apps.accounts.models import User
from apps.common.choices import VisitStatus
import django.utils.timezone

class Visit(BaseModel):
    reference = models.CharField(max_length=50, unique=True, null=True, blank=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT, related_name="visits")
    workflow = models.ForeignKey(Workflow, on_delete=models.PROTECT, related_name="visits")
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="created_visits", default=None, null=True)
    reason = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    entry_time = models.DateTimeField(default=django.utils.timezone.now)
    exit_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    document_retained = models.BooleanField(default=False)
    badge_issued = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=VisitStatus.choices, default=VisitStatus.IN_PROGRESS)

    class Meta:
        db_table = "visits"
        ordering = ["-entry_time"]
        verbose_name = "Visite"
        verbose_name_plural = "Visites"

    def __str__(self):
        return self.reference