from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.

# vai redirecionar a pg da rota inicial p agenda
# def index(request):
#   return redirect('/agenda/')


def lista_eventos(request):
    # evento = Evento.objects.get(id=1)  # pega o obj evento de id 1 do Evento
    # dados = {'evento': evento}  # passa um dicionário p response
    # return render(request, 'agenda.html', dados)  # renderiza o html
    # .all retorna uma lista, então tem q mudar no html
    #usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario) - pega os eventos só do usuário logado no django

    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
