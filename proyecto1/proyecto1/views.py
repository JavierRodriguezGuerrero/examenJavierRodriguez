from django.http import HttpResponse

def saludo(request):  # primera vista
    return HttpResponse("Javier Rodriguez Guerrero")    