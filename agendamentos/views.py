from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from .models import Agendamentos
from django.contrib.auth.decorators import login_required
from .form import AgendamentosForm
from accounts.models import User_Turma
from turmas.models import Turma

#listar
@login_required
def index(request):
    turmas = User_Turma.objects.filter(user=request.user).values_list('turma')
    agendamentos = Agendamentos.objects.filter(turma__in=turmas)
    context = {
        'agendamentos': agendamentos
 }
    return render(request, 'agendamentos/index.html', context)

#detalhar
@login_required
def detalhar(request, agendamentos_id):
    agendamentos = Agendamentos.objects.get(pk = agendamentos_id)
    context = {
        'agendamentos': agendamentos
    }
    return render(request, 'agendamentos/detalhar.html', context)

# @login_required
@login_required
def criar(request):
    if request.user.cargo != 'PF':
        return HttpResponseNotAllowed(['GET', 'POST'])

    if request.method == "POST":
        form = AgendamentosForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect("/agendamentos")
    else:    
        form = AgendamentosForm()
        # Somente turmas que o professor está cadastrado
        turmas = User_Turma.objects.filter(user=request.user).values_list('turma')
        form.fields['turma'].queryset = Turma.objects.filter(pk__in=turmas)

    context = {
        'form': form
    }
    return render(request, 'agendamentos/criar.html', context)

@login_required
def editar(request, agendamentos_id):
    if request.user.cargo != 'PF':
        return HttpResponseNotAllowed(['GET', 'POST'])
    agendamentos = Agendamentos.objects.get(pk = agendamentos_id)
    
    if request.method == "POST":
        form = AgendamentosForm(request.POST, instance=agendamentos)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/agendamentos")
    else:
        form = AgendamentosForm(instance=agendamentos)
        turmas = User_Turma.objects.filter(user=request.user).values_list('turma')
        form.fields['turma'].queryset = Turma.objects.filter(pk__in=turmas)

    
    context = {
        'form': form,
        'agendamentos_id': agendamentos_id
    }
    return render(request, 'agendamentos/editar.html', context)

#excluir
@login_required
def excluir(request, agendamentos_id):
    if request.user.cargo != 'PF':
        return HttpResponseNotAllowed(['GET', 'POST'])
    
    Agendamentos.objects.get(pk=agendamentos_id).delete()
    
    return HttpResponseRedirect("/agendamentos")