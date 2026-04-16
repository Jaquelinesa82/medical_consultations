from django.db import models

from professionals.models import Professional


class Consultation(models.Model):
    professional = models.ForeignKey(
        Professional, on_delete=models.CASCADE, related_name="consultations"
    )
    patient_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-time"]
        verbose_name = "Consultation"
        verbose_name_plural = "Consultations"
        unique_together = ["professional", "date", "time"]

    def __str__(self):
        return f"{self.patient_name} - {self.date} {self.time}"
