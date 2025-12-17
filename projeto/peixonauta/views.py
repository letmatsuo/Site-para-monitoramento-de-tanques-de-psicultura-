from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import LeituraAmonia, LeituraTemperatura, LeituraTurbidez, LeituraPh, LeituraO2

# Página inicial
def index(request):
    return render(request, 'peixonauta/ok.html')

# Exibir as leituras mais recentes
def mostrar_leitura(request):
    amonia = LeituraAmonia.objects.latest('id')
    temperatura = LeituraTemperatura.objects.latest('id')
    ph = LeituraTurbidez.objects.latest('id')
    turbidez = LeituraPh.objects.latest('id')
    oxigenio = LeituraO2.objects.latest('id')

    print(amonia.valor, temperatura.valor, ph.valor, turbidez.valor)

    return render(request, 'peixonauta/ok.html', {
        'amonia': amonia,
        'temperatura': temperatura,
        'ph': ph,
        'turbidez': turbidez,
        'oxigenio': oxigenio
    })

def amonia(request):
    amonia = LeituraAmonia.objects.latest('id')
    alerta = None
    if amonia.valor > 0:  # Supondo que 'valor' seja o campo que representa a leitura
        alerta = "⚠️ Temperatura fora do intervalo ideal! Verifique o sistema."
    return render(request, 'peixonauta/amonia.html', {
        'amonia': amonia,
        'alerta': alerta
    })
def ph(request):
    ph = LeituraPh.objects.latest('id')
    return render(request, 'peixonauta/ph.html', {
        'ph': ph
    })
def temperatura(request):
    temperatura = LeituraTemperatura.objects.latest('id')
    return render(request, 'peixonauta/temperatura.html', {
        'temperatura': temperatura
    })
def turbidez(request):
    turbidez = LeituraTurbidez.objects.latest('id')
    return render(request, 'peixonauta/turbidez.html', {
        'turbidez': turbidez
    })
def oxigenio(request):
    oxigenio = LeituraO2.objects.latest('id')
    return render(request, 'peixonauta/oxigenio.html', {
        'oxigenio': oxigenio
    })

def amonia_view(request):
    return render(request, 'peixonauta/amonia.html')

# API com último, penúltimo e antepenúltimo
def api_dados(request):
    def pegar_ultimos(modelo):
        """
        Retorna último, penúltimo e antepenúltimo valores de um modelo
        """
        registros = list(modelo.objects.order_by('-id')[:3])  # pega os 3 mais recentes
        return {
            "ultimo": registros[0].valor if len(registros) > 0 else None,
            "penultimo": registros[1].valor if len(registros) > 1 else None,
            "antepenultimo": registros[2].valor if len(registros) > 2 else None,
        }

    return JsonResponse({
        "amonia": pegar_ultimos(LeituraAmonia),
        "ph": pegar_ultimos(LeituraPh),
        "temperatura": pegar_ultimos(LeituraTemperatura),
        "turbidez": pegar_ultimos(LeituraTurbidez),
        "oxigenio": pegar_ultimos(LeituraO2),
    })


def amonia(request):
    return render(request, 'peixonauta/amonia.html')

def ph(request):
    return render(request, 'peixonauta/ph.html')

def oxigenio(request):
    return render(request, 'peixonauta/oxigenio.html')

def temperatura(request):
    return render(request, 'peixonauta/temperatura.html')

def turbidez(request):
    return render(request, 'peixonauta/turbidez.html')

def inicio(request):
    return render(request,'peixonauta/ok.html')