from django.urls import path
from .views import esempio_if, es_if_elif_else, es_for

app_name = "seconda_app"

urlpatterns = [
    path("es_if", esempio_if, name="es_if"),
    path("if-else-elif", es_if_elif_else, name="if_else_elif"),
    path("es_for", es_for, name="es_for")
]