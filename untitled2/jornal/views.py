from django.shortcuts import render
from jornal.models import materias
# Create your views here.

def index(request):
    materiass = materias.objects.all()
    return render(request,'home/index.html',{'materias':materiass})
def atualizar(request):
    materiass = materias.objects.all()
    Atualizar = materias.objects.filter(id=4).update(esporte='ciclismo')
    return render(request, 'home/atualizar.html', {'materias': materiass})
def deletar(request):
    materiass = materias.objects.all()
    Deletar = materias.objects.filter(id=5).delete()
    return render(request, 'home/deletar.html', {'materias': materiass})
def inserir(request):
    materiass = materias.objects.all()
    Inserir = materias(esporte='ciclismo')
    Inserir.save()
    return render(request, 'home/inserir.html', {'materias': materiass})
