from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from.models import Funcionario,Movimentacao

from django.urls import reverse_lazy

# Create your views here.


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'matricula', 'cpf', 'vinculo', 'armario', 'gaveta', 'situacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')
    
class MovimentacaoCreate(CreateView):
    model = Movimentacao
    fields = ['setor', 'data', 'funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')


############ UPDATE ############

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome', 'matricula', 'cpf', 'vinculo', 'armario', 'gaveta', 'situacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')
    
class MovimentacaoUpdate(UpdateView):
     model = Movimentacao
     fields = fields = ['setor', 'data', 'funcionario']
     template_name = 'cadastros/form.html'
     success_url = reverse_lazy('listar-funcionario')

############ DELETE ############

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionario')

class MovimentacaoDelete(DeleteView):
    model = Movimentacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionario')
    
    
############ LIST ############

class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'cadastros/listas/index.html'
    
class FuncionarioDeleteList(ListView):
    model = Funcionario
    template_name = 'cadastros/listas/funcionario-delete.html'


class MovimentacaoList(ListView):
    model = Movimentacao
    template_name = 'cadastros/listas/movimentacao.html'
     


