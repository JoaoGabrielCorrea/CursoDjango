from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=255)

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255,blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)

# joao
# 91338822
# superadmin

