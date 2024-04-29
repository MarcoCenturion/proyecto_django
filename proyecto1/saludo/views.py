from django.shortcuts import render

def saludo(request):
    mensaje = 12 * 2
    my_context = {
            "variable1": "Plantilla con contexto",
            "variable2": str(mensaje)
            }
    return render(request,'index.html',my_context)

