from django import forms

from .models import Brand, VehicleModel


class VehicleModelChoiceField(forms.ModelChoiceField):
    """Muestra solo el nombre del modelo (la marca ya está elegida en el otro select)."""

    def label_from_instance(self, obj):
        return obj.name


class VehicleFinderForm(forms.Form):
    """Selector encadenado Marca -> Modelo, resuelto 100% en el servidor."""

    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        label="Marca",
        empty_label="Elegí tu marca",
        widget=forms.Select(attrs={
            "class": "finder-select finder-select--brand",
            # Único fragmento no-Python del formulario: dispara el submit nativo
            # del <form> (recarga de página) para que el servidor recalcule los
            # modelos disponibles. No hay AJAX ni lógica en el cliente.
            "onchange": "this.form.submit();",
        }),
    )
    model = VehicleModelChoiceField(
        queryset=VehicleModel.objects.none(),
        label="Modelo",
        empty_label="Elegí tu modelo",
        widget=forms.Select(attrs={
            "class": "finder-select finder-select--model",
            # Igual que en "brand": recarga la página para que el servidor sepa
            # que ya se eligió el modelo y pueda mostrar el botón "Confirmar".
            "onchange": "this.form.submit();",
        }),
    )

    def __init__(self, *args, brand=None, **kwargs):
        super().__init__(*args, **kwargs)

        if brand is not None:
            self.fields["model"].queryset = VehicleModel.objects.filter(
                brand=brand
            ).select_related("brand")
        else:
            self.fields["model"].empty_label = "Primero elegí una marca"
            self.fields["model"].widget.attrs["disabled"] = True
