from django.db import models


class Foundation(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    social_links = models.JSONField(default=dict, blank=True)  # {"instagram": "...", "x": "..."}
    sector = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Fundación"
        verbose_name_plural = "Fundaciones"

    def __str__(self):
        return self.name


class Event(models.Model):
    foundation = models.ForeignKey(Foundation, on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    link = models.URLField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-start_date"]
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return f"{self.name} ({self.foundation})"