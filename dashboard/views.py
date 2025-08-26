from django.shortcuts import render

def inicio(request):
    return render(request, 'dashboard/inicio.html', {"page": "inicio"})

def povos(request):
    return render(request, 'dashboard/povos.html', {"page": "povos"})
