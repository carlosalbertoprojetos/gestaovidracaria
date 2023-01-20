from django.urls import path

from .views import (
                    funcionario_delete, funcionario_list_create, funcionario_update,
                    filho_create_view,filho_list, filho_update_view,filho_delete
                    )
 

app_name = 'funcionario'

urlpatterns = [
    
    #===================================================================================
    #FUNCIONARIO
    path('list/', funcionario_list_create, name='funcionario_list_create'),    
    path('<int:pk>/edit/', funcionario_update, name='funcionario_update'),
    path('<int:pk>/delete/', funcionario_delete, name='funcionario_delete'),
    #===================================================================================
    #FILHO
    path('<int:funcionario_id>/filho/', filho_create_view, name='filho_create'),
    path('<int:pk>/filho/detail/', filho_list, name='filho_list'),
    path('<int:funcionario_id>/filho/<int:pk>/update/', filho_update_view, name='filho_update'),
    path('<int:funcionario_id>/filho/<int:pk>/delete/', filho_delete, name='filho_delete'), 
]