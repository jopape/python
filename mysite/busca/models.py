from django.db import models
import datetime

class Tipo(models.Model):
	nome_tipo = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nome_tipo
		
class Curso(models.Model):
	nome_curso = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.nome_curso
	
class Projeto(models.Model):
	titulo = models.CharField(max_length=200)
	autor = models.CharField(max_length=300)
	orientador = models.CharField(max_length=300)
	ano = models.IntegerField()
	arquivo = models.CharField(max_length=70)
	palavras_chave = models.CharField(max_length=100)
	tipo = models.ForeignKey(Tipo)
	curso = models.ForeignKey(Curso)

	
	def __unicode__(self):
		return self.titulo
	
	