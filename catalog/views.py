from django.conf import settings
from django.shortcuts import render

from .models import Brand


def index(request):
    """Landing page: hero + buscador de marcas/modelos."""
    brands = Brand.objects.prefetch_related("models").all()
    context = {
        "brands": brands,
        "whatsapp_number": getattr(settings, "WHATSAPP_NUMBER", "5491112345678"),
        "whatsapp_message": "Hola! Quiero consultar por un amortiguador de capot.",
    }
    return render(request, "catalog/index.html", context)
