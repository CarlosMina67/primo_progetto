from django.urls import path
from prova_pratica_1_B.views import index, massimo, pari, studenti
from . import views
app_name = "prova_pratica_1_B"
urlpatterns = [
    path('', views.index ,name='index'),
    path('view_x/', views.massimo, name='massimo' ),
    path('view_y/', views.pari, name='pari'),
    path('view_z/', views.studenti, name='studenti'),
]