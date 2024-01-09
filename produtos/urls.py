from django.urls import path

from . import views

app_name = "produtos"

urlpatterns = [
    path("", views.ProdutosView.as_view(), name="index"),
    path("lista/", views.ProdutosListView.as_view(), name="lista_produtos"),
    path("novo/", views.ProdutoCreateView.as_view(), name="novo_produto"),
    path("delete/<str:pk>", views.ProdutoDeleteView.as_view(), name="deleta_produto"),
    path("alterar/<str:pk>", views.ProdutoUpdateView.as_view(), name="alterar_produto"),
]