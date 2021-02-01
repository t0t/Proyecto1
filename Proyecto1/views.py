from django.http import HttpResponse
import datetime
from django.template import Template, Context
# from django.template.loader import get_template
from django.shortcuts import render

# Vista Artwork
def artwork(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "artwork.html", {"dameFecha": fecha_actual})

# Vista About
def about(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "about.html", {"dameFecha": fecha_actual})

# Vista saludo
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): # nuestra primera vista para la HOME
    p1 = Persona("Sergio", "Forés")
    temasCurso= ["Plantillas","Modelos","Formularios","Vistas","Deploy del App"]
    ahora = datetime.datetime.now()

    ctx = {
        "nombre_persona": p1.nombre,
        "apellido_persona": p1.apellido,
        "momento_actual": ahora,
        "temas": temasCurso
    } 

    return render(request, "miplantilla.html", ctx)



def despedida(request): # nuestra segunda vista
    return HttpResponse("Adiossssss") # nos devuelve una respuesta

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
        <body>
            <h1>Fecha y hora actuales:</h1>
            <h2>{}</h2>
        </body>
    </html>
    """.format(fecha_actual)
    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    periodo = agno - 2021
    edadFutura = edad + periodo

    documento = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Testing Django</title>
    </head>
    <body>
        <p>En el año: {}</p>
        <p>tendrás: {} años</p>
        <input type="email" id="email" name="email">
    </body>
    </html>
    """.format(agno,edadFutura)

    return HttpResponse(documento)
    