from django.db import models
from backend.apps.common.models import BaseModel
from backend.apps.common.choices import DocumentType, Gender

class Visitor(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    document_type = models.CharField(
        max_length=20,
        choices=DocumentType.choices
    )
    document_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    expired_date = models.DateField(null =False, blank=False, required=True)
    issue_date = models.DateField(null =False, blank=False, required=True)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices
    )
    nationality = models.CharField(max_length=100)
    birth_date = models.DateField(null =True, blank=True)
    birth_place = models.CharField(max_length=100, null=True, blank=True )

    class Meta:
        db_table = "Visitor"
        ordering = ["last_name", "first_name"]
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.document_type}: {self.document_number})"


