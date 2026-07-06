from django.conf import settings
from django.shortcuts import render

def index(request):
    """Landing page: hero + buscador de marcas/modelos."""
    
    # Este es tu diccionario manual con todos los autos
    catalogo_autos = {
        "Volkswagen": [
            "Gol", "Gol Trend", "Voyage", "Fox", "Suran", 
            "Bora", "Vento", "Polo", "Virtus", "Amarok", 
            "Saveiro", "Taos", "Tiguan",
        ],
        "Chevrolet": [
            "Corsa", "Classic", "Onix", "Prisma", "Cruze", 
            "Tracker", "S10", "Spin", "Agile", "Meriva",
        ],
        "Fiat": [
            "Uno", "Palio", "Siena", "Cronos", "Argo", 
            "Toro", "Strada", "Fiorino", "Mobi", "Punto",
        ],
        "Renault": [
            "Clio", "Sandero", "Logan", "Duster", "Kangoo", 
            "Oroch", "Megane", "Symbol", "Captur", "Kwid",
        ],
        "Peugeot": [
            "206", "207", "208", "2008", "307", "308", 
            "3008", "Partner", "Expert", "Boxer",
        ]
    }

    # Juntamos tus autos con los datos de WhatsApp que ya venían en el código original
    context = {
        "catalogo": catalogo_autos,
        "whatsapp_number": getattr(settings, "WHATSAAPP_NUMBER", "5491112345678"),
        "whatsapp_message": "Hola! Quiero consultar por un amortiguador de capot.",
    }

    # Le mandamos todo al index.html
    return render(request, "catalog/index.html", context)