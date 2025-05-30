import requests
from icalendar import Calendar

def obtener_reservas_airbnb(url):
    """ Descarga y parsea un calendario .ics de Airbnb """
    response = requests.get(url)
    
    if response.status_code == 200:
        cal = Calendar.from_ical(response.content)
        reservas = []

        for component in cal.walk():
            if component.name == "VEVENT":
                reservas.append({
                    "titulo": component.get('summary'),
                    "inicio": component.get('dtstart').dt,
                    "fin": component.get('dtend').dt
                })

        return reservas
    else:
        return None
