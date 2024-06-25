from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Pestaña de inicio


def inicio(request):
    return HttpResponse("Inicio")


def carrito(request):
    return HttpResponse("Carrito")


def registro(request):
    return HttpResponse("registro")


def ingreso_usuario(request):
    return HttpResponse("inicio sesión")


def menus(request):
    return HttpResponse("Ventana Menús")
