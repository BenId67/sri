from django.db import models


class DocumentType(models.TextChoices):
    CNIB = "CNIB", "CNIB"
    PASSPORT = "PASSPORT", "Passeport"


class Gender(models.TextChoices):
    MALE = "M", "Masculin"
    FEMALE = "F", "Féminin"