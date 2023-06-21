from typing import Any
from django.db.models.query import QuerySet
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from.models import Funcionario,Movimentacao

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


class FuncionarioCreate(LoginRequiredMixin ,CreateView):
    login_url = reverse_lazy('login')
    model = Funcionario
    fields = ['nome', 'matricula', 'cpf', 'vinculo', 'armario', 'gaveta', 'situacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')
    
    
    
class MovimentacaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Movimentacao
    fields = ['setor', 'data', 'funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-movimentacao')


############ UPDATE ############

class FuncionarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Funcionario
    fields = ['nome', 'matricula', 'cpf', 'vinculo', 'armario', 'gaveta', 'situacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')
    
class MovimentacaoUpdate(LoginRequiredMixin, UpdateView):
     login_url = reverse_lazy('login')
     model = Movimentacao
     fields = fields = ['setor', 'data', 'funcionario']
     template_name = 'cadastros/form.html'
     success_url = reverse_lazy('listar-movimentacao')

############ DELETE ############

class FuncionarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionario')

class MovimentacaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Movimentacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-movimentacao')
    
    
############ LIST ############

class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'cadastros/listas/index.html'
    
    def get_queryset(self):
        
        txt_nome = self.request.GET.get('nome', '')
        
        funcionario = Funcionario.objects.filter(nome__icontains=txt_nome)
        
        return funcionario  
    
class FuncionarioDeleteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/listas/funcionario-delete.html'
    
    def get_queryset(self):
        
        txt_nome = self.request.GET.get('nome', '')
        
        funcionario = Funcionario.objects.filter(nome__icontains=txt_nome)
        
        return funcionario 


class MovimentacaoList(ListView):
    model = Movimentacao
    template_name = 'cadastros/listas/movimentacao.html'
    
     


