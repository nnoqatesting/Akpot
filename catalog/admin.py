from django.contrib import admin
from .models import Brand, VehicleModel


class VehicleModelInline(admin.TabularInline):
    model = VehicleModel
    extra = 1


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [VehicleModelInline]


@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "order")
    list_filter = ("brand",)
    prepopulated_fields = {"slug": ("name",)}
