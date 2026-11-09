from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista

# Create your views here.
def home(request):
    context = {
        "articoli": Articolo.objects.select_related("giornalista").all(),
        "giornalisti": Giornalista.objects.all(),
    }
    return render(request, "news/homepage.html", context)


def articoloDetailView(request, pk):
    # articolo = Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "news/articolo_detail.html", context)


def listaArticoli(request, pk=None):
    # Se pk non viene passato, mostriamo tutti gli articoli disponibili.
    if pk is None:
        articoli = Articolo.objects.all()
        giornalista = None
        mostra_giornalista = False
        titolo = "Tutti gli Articoli"
    else:
        # Se pk viene passato, recuperiamo il giornalista corrispondente.
        giornalista = get_object_or_404(Giornalista, pk=pk)

        # Query: seleziona tutti gli articoli del giornalista specificato.
        # In SQL equivale a: SELECT * FROM news_articolo WHERE giornalista_id = pk
        articoli = Articolo.objects.filter(giornalista_id=pk)
        mostra_giornalista = True
        titolo = "Articoli di un giornalista"

    context = {
        "giornalista": giornalista,
        "articoli": articoli,
        "mostra_giornalista": mostra_giornalista,
        "titolo": titolo,
    }
    return render(request, "lista_articoli.html", context)


def queryBase(request):
    context = {
        "articoli_cognome": [],
        "numero_totale_articoli": [],
        "numero_articoli_giornalista": [],
        "articoli_ordinati": [],
        "articoli_senza_visualizzazioni": [],
        "articolo_piu_visualizzato": [],
        "giornalisti_data": [],
        "articoli_del_giorno": [],
        "articoli_periodo": [],
        "giornalisti_nati": [],
        "giornalista_giovane": [],
        "giornalista_anziano": [],
        "ultimi_5": [],
        "articoli_minime_visualizzazioni": [],
        "articoli_parola": [],
    }
    return render(request, "news/query.html", context)