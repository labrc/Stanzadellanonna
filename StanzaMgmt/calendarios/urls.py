from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('eventos/', views.obtener_eventos_ics, name='eventos_ics'),
]