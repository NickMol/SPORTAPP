from django.shortcuts import render
from django.http import HttpResponse

def homepagina(request):
    return HttpResponse("Dit is de homepagina")

def over_ons(request):
    return HttpResponse("Dit is de over ons pagina")




