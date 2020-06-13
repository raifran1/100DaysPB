from django.contrib import admin
from .models import Aula, Comentario

class AulaAdmin(admin.ModelAdmin):
	list_display = ['title', 'subTitle']
	search_fields = ['title', 'subTitle']

	#def get_queryset(self, request):
		#return Aula.objects.filter(ativado = True)

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ['aulaCodigo', 'ativado', 'nameAutor', 'coment']
	search_fields = ['nameAutor', 'coment']

admin.site.register(Aula, AulaAdmin)
admin.site.register(Comentario, ComentarioAdmin)