'''
from django.http import HttpResponse
from .models import Articolo, Giornalista
from django.shortcuts import render


 2 VERSIONE (Concatenazione di stringhe)
 def home(request):
     a = ""
     g = ""
     
     for art in Articolo.objects.all():
         a += (art.titolo + "<br>")
 
     for gio in Giornalista.objects.all():
         g += (gio.nome + "<br>")
        
     response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g
 
     return HttpResponse("<h1>" + response + "</h1>")

 3 VERSIONE  (Costruzione manuale di stringhe e HttpResponse)
 from django.http import HttpResponse

 def home(request):
     a = []
     g = []

     for art in Articolo.objects.all():
         a.append(art.titolo)

     for gio in Giornalista.objects.all():
         g.append(gio.nome)
 
     response = str(a) + "<br>" + str(g)
     print(response)
 
     return HttpResponse("<h1>" + response + "</h1>")

# 4 VERSIONE (Utilizzo dei Template HTML e della funzione render)
def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage.html", context)
'''

from django.urls import path
from .views import home, articoloDetailView

app_name = "news"

urlpatterns = [
    path("", home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
]