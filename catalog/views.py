import urllib.parse

from django.conf import settings
from django.shortcuts import redirect, render

from .forms import VehicleFinderForm
from .models import Brand, VehicleModel


def index(request):
    """Landing page: hero + buscador de marca/modelo (100% server-side, sin JS)."""

    selected_brand = None
    brand_id = request.GET.get("brand")
    if brand_id:
        selected_brand = Brand.objects.filter(pk=brand_id).first()

    form = VehicleFinderForm(request.GET or None, brand=selected_brand)

    # El botón "Confirmar" solo se muestra si el modelo elegido existe
    # y pertenece realmente a la marca seleccionada (evita mostrarlo con
    # un valor de modelo que quedó obsoleto tras cambiar de marca).
    model_id = request.GET.get("model")
    mostrar_confirmar = bool(
        selected_brand and model_id
        and VehicleModel.objects.filter(pk=model_id, brand=selected_brand).exists()
    )

    confirmacion = None
    if "consultar" in request.GET and form.is_valid():
        model = form.cleaned_data["model"]
        mensaje = (
            f"Hola! Quiero consultar por un amortiguador de capot "
            f"para {model.brand.name} {model.name}."
        )
        # Redirect a WhatsApp desactivado a pedido: por ahora "Confirmar" solo
        # valida la selección y la muestra en pantalla. Para reactivarlo, descomentar:
        #
        # whatsapp_number = getattr(settings, "WHATSAPP_NUMBER", "5491112345678")
        # whatsapp_url = f"https://wa.me/{whatsapp_number}?text={urllib.parse.quote(mensaje)}"
        # return redirect(whatsapp_url)
        confirmacion = mensaje

    context = {
        "form": form,
        "mostrar_confirmar": mostrar_confirmar,
        "confirmacion": confirmacion,
        "whatsapp_number": getattr(settings, "WHATSAPP_NUMBER", "5491112345678"),
        "whatsapp_message": "Hola! Quiero consultar por un amortiguador de capot.",
    }
    return render(request, "catalog/index.html", context)
