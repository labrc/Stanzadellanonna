
from django.shortcuts import render
from .utils import obtener_reservas_airbnb
import requests 
from icalendar import Calendar
from django.http import JsonResponse

AIRBNB_CALENDAR_URL = "https://www.airbnb.com.ar/calendar/ical/10614885.ics?s=899c1e152850cf672d6c2f542d8e048f"

def calendario(request):
    reservas = obtener_reservas_airbnb(AIRBNB_CALENDAR_URL)
    return render(request, "calendario.html", {"reservas": reservas})

from django.http import JsonResponse


def obtener_eventos_ics(request):
    """ Descarga y convierte el archivo .ics a JSON para FullCalendar """
    response = requests.get(AIRBNB_CALENDAR_URL)

    if response.status_code == 200:
        cal = Calendar.from_ical(response.content)
        eventos = []

        for component in cal.walk():
            if component.name == "VEVENT":
                eventos.append({
                    "title": component.get('summary'),
                    "start": component.get('dtstart').dt.isoformat(),
                    "end": component.get('dtend').dt.isoformat() if component.get('dtend') else None
                })

        return JsonResponse(eventos, safe=False)
    else:
        return JsonResponse({"error": "No se pudo descargar el calendario"}, status=400)