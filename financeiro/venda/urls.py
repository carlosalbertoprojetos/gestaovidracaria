from django.urls import path

from . import views as v

app_name = 'venda'

urlpatterns = [

    #VENDA
    path('', v.venda_create, name='venda_create'),
    path('list/', v.venda_list_create, name='venda_list_create'),
    path('<int:pk>/edit/', v.venda_update, name='venda_update'),
    path('<int:pk>/edit2/', v.venda_update2, name='venda_update2'),
    path('<int:pk>/delete/', v.venda_delete, name='venda_delete'),
    #===================================================================================
    
    #VENDA PRODUTOS
    path('<int:venda_id>/produtos/', v.venda_produto_create_view, name='venda_produto_create'),
    path('<int:pk>/produtos/detail/', v.venda_produto_list, name='venda_produto_list'),
    path('<int:venda_id>/produtos/<int:pk>/update/', v.venda_produto_update_view, name='venda_produto_update_view'),
    path('<int:venda_id>/produtos/<int:pk>/delete/', v.venda_produto_delete, name='venda_produto_delete'),
    #===================================================================================

    #VENDA PRESTAÇÕES
    path('<int:venda_id>/prestacao/', v.venda_prestacao_create_view, name='venda_prestacao_create'),
    path('<int:pk>/prestacao/detail/', v.venda_prestacao_list, name='venda_prestacao_list'),
    path('<int:venda_id>/prestacao/<int:pk>/update/', v.venda_prestacao_update_view, name='venda_prestacao_update'),
    path('<int:venda_id>/prestcao/<int:pk>/delete/', v.venda_prestacao_delete, name='venda_prestacao_delete'), 
    path('areceber/', v.contas_receber, name='contas_receber'),
    
    path('contas/areceber/', v.ano_dropdown, name='ano_dropdown'),
    path(
        'ano/', v.meses_choices_ajax, name='meses_choices_ajax'
    ),    
    path(
        'periodo/',
        v.meses_prestacoes_ajax,
        name='meses_prestacoes_ajax'
    ), 
]