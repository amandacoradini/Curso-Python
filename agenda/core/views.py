from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# vai redirecionar a pg da rota inicial p agenda
# def index(request):
#   return redirect('/agenda/')


# vai chamar a pg html do login
def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    # se a requisição for do tipo post
    if request.POST:
        # pega o valor de username do formulário
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        # se o usuário n é vazio
        if usuario is not None:
            login(request, usuario)
            # volta p pg inicial, passa pelo decorador e prossegue
            return redirect('/')
        else:
            # se n conseguir fazer o login ele manda uma msg
            messages.error(request, "Usuário ou senha inválidos")
        return redirect('/')  # redireciona p a pg de login


# o usuário só pode acessar a agenda se estiver logado(p usar decorator usa @)
# se deslogar a tela da erro automaticamente.
# Caso n esteja logado, vamos redirecioná-lo a pg de login


@login_required(login_url='/login/')
def lista_eventos(request):
    # evento = Evento.objects.get(id=1)  # pega o obj evento de id 1 do Evento
    # dados = {'evento': evento}  # passa um dicionário p response
    # return render(request, 'agenda.html', dados)  # renderiza o html
    # .all retorna uma lista, então tem q mudar no html
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario) - pega os eventos só do usuário logado no django
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')

    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')

        if id_evento:
            # se o id existe faz o update dele
            Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                       data_evento=data_evento,
                                                       descricao=descricao
                                                       )
        else:
            # se n exite cria ele
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)

    return redirect('/')


@login_required(login_url='/login/')
# deletar um evento
def delete_evento(request, id_evento):
    # só o usuário do evento q pode excluir ele
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')
