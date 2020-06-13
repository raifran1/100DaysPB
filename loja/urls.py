from django.urls import path
from .views import listar_produtos

urlpatterns = [
    path('<int:id>/', listar_produtos, name='produtos'),
]
