from django.shortcuts import render
import datetime

def esempio_if(request):
    dic = { 'var1' : 200, 'var2' : 200, 'var3' : 300 }
    return render(request, "es_if.html", dic)

# Nuova view per l'esercizio if-else-elif
def es_if_elif_else(request):
    dic = {
        'var1': 100,
        'var2': 200,
        'var3': 300
    }
    return render(request, "es_if_elif_else.html", dic)

def es_for(request):
    dic = {
        'list1': [1, datetime.date(2019, 7, 16), 'Do not give up!'],
        'list2': [1, datetime.date(2019, 7, 16), 'Do not give up!'],
        'my_dict': {'chiave1': 'Valore 1', 'chiave2': 'Valore 2'}
    }
    return render(request, "es_for.html", dic)