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