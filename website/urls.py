from django.urls import path
from .views import index, detail, saveComentario, admin2, editarAula, cadastrarAula, removerAula

urlpatterns = [
    path('', index, name='home'),
    path('aula/<int:idAula>/', detail, name='aula_detail'),
    path('save-comentario/<int:Aulaid>', saveComentario, name='save-comentario'),
    path('admin2/', admin2, name='admin2'),
    path('admin2/post_aula/', cadastrarAula, name='post_aula'),
    path('admin2/editar_aula/<int:Aulaid>', editarAula, name='editarAula'),
    path('admin2/remover_aula/<int:Aulaid>', removerAula, name='removerAula'),
]
