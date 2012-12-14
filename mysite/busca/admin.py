from busca.models import *
from django.contrib import admin


class TipoAdmin(admin.ModelAdmin):
	fields = ['nome_tipo']
	
	
	
class CursoAdmin(admin.ModelAdmin):
	fields = ['nome_curso']
	
class ProjetoAdmin(admin.ModelAdmin):
	#so pode ter um fields ou um fieldsets
	#fields = ['autor','titulo','orientador','ano','arquivo','palavras_chave','tipo','curso']
	
	#list_display = ('Tipo','Autor(es)','Orientador(es)','Ano','Curso','Arquivo(pdf)')
	fieldsets = [
		(None, {'fields':['tipo','autor','orientador','ano','curso',]}),
		('Arquivo', {'fields' :['arquivo'], 'classes': ['collapse']})]
		
	

admin.site.register(Tipo,TipoAdmin)
admin.site.register(Curso)
admin.site.register(Projeto,ProjetoAdmin)