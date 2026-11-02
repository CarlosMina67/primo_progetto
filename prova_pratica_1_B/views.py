import random
from django.shortcuts import render

def index(request):
    """
    View per la pagina principale (index) con i collegamenti alle altre tre view.
    """
    return render(request, 'prova_pratica_1_B/index.html')


def massimo(request):
    """
    Genera 3 numeri casuali da 1 a 20 e individua il massimo.
    """
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    n3 = random.randint(1, 20)
    valore_massimo = max(n1, n2, n3)

    context = {
        'n1': n1,
        'n2': n2,
        'n3': n3,
        'massimo': valore_massimo,
    }
    return render(request, 'prova_pratica_1_B/massimo.html', context)


def pari(request):
    """
    Genera una lista di 30 numeri casuali da 1 a 20 e conta quanti sono pari.
    """
    numeri = [random.randint(1, 20) for _ in range(30)]
    conteggio_pari = sum(1 for n in numeri if n % 2 == 0)

    context = {
        'numeri': numeri,
        'conteggio_pari': conteggio_pari,
    }
    return render(request, 'prova_pratica_1_B/pari.html', context)


def studenti(request):
    """
    Visualizza l'elenco degli studenti e la relativa presenza/assenza.
    """
    dizionario_studenti = {
        'Mario Rossi': True,
        'Luigi Bianchi': False,
        'Giulia Verdi': True,
        'Francesca Neri': False,
        'Alessandro Gialli': True,
        'Sara Esposito': True,
    }

    context = {
        'studenti': dizionario_studenti,
    }
    return render(request, 'prova_pratica_1_B/studenti.html', context)