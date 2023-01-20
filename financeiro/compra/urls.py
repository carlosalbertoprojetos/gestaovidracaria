from django.urls import path

from . import views as v

app_name = 'compra'

urlpatterns = [
    #===================================================================================
    #COMPRA
    path('', v.compra_create, name='compra_create'),
    path('lista/geral/', v.lista_geral, name='lista_geral'),
    path('list/', v.compra_list_create, name='compra_list_create'),
    path('<int:pk>/edit/', v.compra_update, name='compra_update'),
    path('<int:pk>/edit2/', v.compra_update2, name='compra_update2'),
    path('<int:pk>/delete/', v.compra_delete, name='compra_delete'),

    #===================================================================================
    #COMPRA PRODUTOS
    path('<int:compra_id>/produtos/', v.compra_produto_create_view, name='compra_produto_create'),
    path('<int:pk>/produtos/detail/', v.compra_produto_list, name='compra_produto_list'),
    path('<int:compra_id>/produtos/<int:pk>/update/', v.compra_produto_update_view, name='compra_produto_update_view'),
    path('<int:compra_id>/produtos/<int:pk>/delete/', v.compra_produto_delete, name='compra_produto_delete'), 

    #===================================================================================
    #COMPRA PRESTAÇÕES
    path('<int:compra_id>/prestacao/', v.compra_prestacao_create_view, name='compra_prestacao_create'),
    path('<int:pk>/prestacao/detail/', v.compra_prestacao_list, name='compra_prestacao_list'),
    path('<int:compra_id>/prestacao/<int:pk>/update/', v.compra_prestacao_update_view, name='compra_prestacao_update'),
    path('<int:compra_id>/prestcao/<int:pk>/delete/', v.compra_prestacao_delete, name='compra_prestacao_delete'),

    path('contas/', v.ano_dropdown, name='ano_dropdown'),
    path(
        'contas/apagar/', v.meses_choices_ajax, name='meses_choices_ajax'
    ),
    path(
        'contas/apagar/periodo/',
        v.meses_prestacoes_ajax,
        name='meses_prestacoes_ajax'
    ),   
]