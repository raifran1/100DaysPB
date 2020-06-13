from django import forms
from .models import Aula

class AulaForm(forms.ModelForm):
	class Meta:
		model = Aula # sobrescreve o atributo model da classe Meta

		#fields = ('title', 'subTitle', 'autor', 'aulaNumber', 'video', 'text', 'image', 'publicado')
		exclude = ('cadastrado', 'alterado', 'ativado')

		# sobrescreve o atributo fields da classe Meta
		# se a quantidade de intens a adicionar for maior que a quantidade de fields que nao vou renderizar
			# usar o fileds = ('intem_a_ser_renderizado',)
		# se não
			# usar o exclude = ('intem_nao_renderiza',)