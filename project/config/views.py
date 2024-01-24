from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡hola!")

def saludo2(request):
    nombre = input("*** Ingresa tu nombre: ")
    return HttpResponse(f"Hola <h1> {nombre} </h1>")

def nombre(request, nombre: str, apellido: str):
    return HttpResponse(f"{apellido.upper()}, {nombre}")

def fecha_hora(request):
    from datetime import datetime
    ahora = datetime.now().strftime(r'%d/%m/%Y %H:%M:%S')
    return HttpResponse(ahora)

def tirar_dado(request):
    import random
    mi_numero = random.randint(1, 6)
    if mi_numero == 6:
        return HttpResponse (f'<h1> Has tirado el dado: 🎲 {mi_numero} 😊 tuviste suerte </h1>' )
    else:
        return HttpResponse (f'<h1> Has tirado el dado: 🎲 {mi_numero} siguen intentando </h1>' )
        