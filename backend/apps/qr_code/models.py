from django.db import models
from apps.common.models import BaseModel
from apps.visits.models import Visit


class QRCode(BaseModel):
    visit = models.OneToOneField(
        Visit,
        on_delete=models.CASCADE,
        related_name="qr_code"
    )

    code = models.CharField(
        max_length=255,
        unique=True
    )

    generated_at = models.DateTimeField(
        auto_now_add=True
    )

    scanned_at = models.DateTimeField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        db_table = "qr_codes"
        ordering = ["-generated_at"]
        verbose_name = "QR Code"
        verbose_name_plural = "QR Codes"

    def __str__(self):
        return self.code