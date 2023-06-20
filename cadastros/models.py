from django.db import models
import datetime

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=6, verbose_name="Matrícula")
    cpf = models.IntegerField(verbose_name="CPF")
    vinculo = models.CharField(max_length=12, verbose_name="Vínculo")
    armario = models.IntegerField(verbose_name="Armário")
    gaveta = models.IntegerField(verbose_name="Gaveta")
    situacao = models.BooleanField(default=True)
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.matricula)
    
class Movimentacao(models.Model):
    setor = models.CharField(max_length=15, verbose_name="Setor")
    data = models.DateField(default=datetime.date.today)
    
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    
    def __str__(self):
        return "Armário: {}, Gaveta:{} (Setor: {}, Data:{})".format(self.funcionario.armario, self.funcionario.gaveta, self.setor, self.data.strftime('%d/%m/%Y'))

