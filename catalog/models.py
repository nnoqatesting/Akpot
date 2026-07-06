from django.db import models
from django.utils.text import slugify


class Brand(models.Model):
    """Marca de vehículo (ej: Volkswagen, Chevrolet)."""

    name = models.CharField("Nombre", max_length=60, unique=True)
    slug = models.SlugField(max_length=70, unique=True, blank=True)
    order = models.PositiveIntegerField("Orden", default=0)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class VehicleModel(models.Model):
    """Modelo de vehículo asociado a una marca (ej: Gol, Corsa)."""

    brand = models.ForeignKey(
        Brand, related_name="models", on_delete=models.CASCADE
    )
    name = models.CharField("Modelo", max_length=60)
    slug = models.SlugField(max_length=70, blank=True)
    order = models.PositiveIntegerField("Orden", default=0)

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
        ordering = ["order", "name"]
        unique_together = ("brand", "slug")

    def __str__(self):
        return f"{self.brand.name} {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
