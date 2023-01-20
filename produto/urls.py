from django.urls import path

from .views import (
                    produto_delete, produto_list_create, produto_update, tributo_create_view,
                    tributo_list, tributo_update_view,tributo_delete, categoria_delete,
                    categoria_list_create, categoria_update, unimed_delete, unimed_update,
                    unimed_list_create, tabela_list,                    
                    calculos_tritubos_lista
                    )
 

app_name = 'produto'

urlpatterns = [

    #CATEGORIAS
    path('categoria/list/', categoria_list_create, name='categoria_list_create'),    
    path('<int:pk>/categoria/edit/', categoria_update, name='categoria_update'),
    path('<int:pk>/categoria/delete/', categoria_delete, name='categoria_delete'),    
    #===================================================================================

    #UNIDADE DE MEDIDA
    path('unimed/list/', unimed_list_create, name='unimed_list_create'),    
    path('<int:pk>/unimed/edit/', unimed_update, name='unimed_update'),
    path('<int:pk>/unimed/delete/', unimed_delete, name='unimed_delete'),    
    #===================================================================================

    #PRODUTOS
    path('list/', produto_list_create, name='produto_list_create'),    
    path('<int:pk>/edit/', produto_update, name='produto_update'),
    path('<int:pk>/delete/', produto_delete, name='produto_delete'),
    #===================================================================================
    #TRIBUTOS
    path('<int:produto_id>/tributo/', tributo_create_view, name='tributo_create'),
    path('<int:pk>/tributo/detail/', tributo_list, name='tributo_list'),
    path('<int:produto_id>/tributo/<int:pk>/update/', tributo_update_view, name='tributo_update'),
    path('<int:produto_id>/tributo/<int:pk>/delete/', tributo_delete, name='tributo_delete'),
    path('<int:produto_id>/tabela/', tabela_list, name='tabela_list'),    
    
    path('lista/', calculos_tritubos_lista, name="calculos_tritubos_lista")
]