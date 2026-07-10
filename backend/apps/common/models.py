<<<<<<< HEAD
from uuid import uuid4
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    
=======
from django.db import models

# Create your models here.
>>>>>>> eaa11b1226c8ceb215bbde6c2603c2a50c9da98a
