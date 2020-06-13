from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Aula, Comentario
from .forms import AulaForm
from django.utils import timezone

from django.contrib import messages

def index(request):
	aulas = Aula.objects.filter(ativado=True)

	dados = {
		'Aulas': aulas
	}
	return render(request, 'index.html', dados)

def detail(request, idAula):

	aulas = Aula.objects.get(id=idAula)
	comentarios = Comentario.objects.filter(aulaCodigo=idAula)

	dados = {
		'Aulas': aulas,
		'Comentarios': comentarios
	}
	return render(request, 'detail.html', dados)

def saveComentario(request, Aulaid):
	aulas = Aula.objects.get(id=Aulaid)

	Comentario.objects.create(
		aulaCodigo = aulas,
		nameAutor = request.POST['nome'],
		coment = request.POST['comentario'],
		sexo = request.POST['sexo'],
	)

	return redirect('aula_detail', Aulaid)

def admin2(request):
	aulas = Aula.objects.all()

	dados = {
		'Aulas': aulas
	}

	return render(request, 'admin2.html', dados)

def cadastrarAula(request):
	form_class = AulaForm
	form = form_class(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			#TODO: usar request.FILES para carregar as imagens do post
			form = AulaForm(request.POST, request.FILES)
			#f = form.save()
			f = form.save(commit=False) # esperar um tempinho antes de salvar
			# f.autor = request.user  #pega um usuário
			#f.save() # salvar o formulário
			print('imagem: ', f.image)
			f.cadastrado = timezone.now()
			f.alterado = timezone.now()
			f.save()
			return redirect('admin2')
	else:
		form = AulaForm() #exibir o formulário

	return render(request, 'add_aula.html', {'form':form})

def editarAula(request, Aulaid):
	form_class = AulaForm
	form = form_class(request.POST or None)
	aula = get_object_or_404(Aula, id=Aulaid)
	if request.method == 'POST':
		form = AulaForm(request.POST, request.FILES, instance=aula)
		if form.is_valid():
			f = form.save(commit=False) # esperar um tempinho antes de salvar
			# f.image = request.POST.get('image')
			print('imagem: ', f.image)
			f.cadastrado = timezone.now()
			f.alterado = timezone.now()
			f.save()
			return redirect('admin2')
	else:
		form = AulaForm(instance=aula) #exibir o formulário

	return render(request, 'add_aula.html', {'form':form})

def removerAula(request, Aulaid):
	aula = Aula.objects.get(id=Aulaid)
	aula.delete()

	return redirect('admin2')