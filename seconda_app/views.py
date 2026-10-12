from django.shortcuts import render

def esempio_if(request):
    # Creating a dictionary of key-value pairs
    dic = {
        'var1': 200,
        'var2': 200,
        'var3': 300
    }
    # Calling the render() method to render the request from es_if.html
    return render(request, "es_if.html", dic)