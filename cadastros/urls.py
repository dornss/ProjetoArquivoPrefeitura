from django.urls import path
from .views import FuncionarioCreate, MovimentacaoCreate
from .views import FuncionarioUpdate, MovimentacaoUpdate
from .views import FuncionarioDelete, MovimentacaoDelete
from .views import FuncionarioList, MovimentacaoList, FuncionarioDeleteList

urlpatterns = [
    path('cadastrar/funcionario/', FuncionarioCreate.as_view(), name="cadastrar-funcionario"),
    path('cadastrar/movimentacao/', MovimentacaoCreate.as_view(), name="cadastrar-movimentacao"),
    
    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name="editar-funcionario"),
    path('editar/movimentacao/<int:pk>/', MovimentacaoUpdate.as_view(), name="editar-movimentacao"),
    
    path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name="excluir-funcionario"),
    path('excluir/movimentacao/<int:pk>/', MovimentacaoDelete.as_view(), name="excluir-movimentacao"),
    
    path('listar/funcionario/', FuncionarioList.as_view(), name="listar-funcionario"),
    path('listar/movimentacao/', MovimentacaoList.as_view(), name="listar-movimentacao"),
    
    path('listar/funcionario/delete', FuncionarioDeleteList.as_view(), name="listar-funcionario-delete"),
]