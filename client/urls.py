from django.urls import path

from .views import (
                    client_delete, client_list_create, client_update, obra_create_view,obra_list,
                    obra_update_view,obra_delete
                    )
 

app_name = 'client'

urlpatterns = [
    
    #===================================================================================
    #CLIENTE
    path('list/', client_list_create, name='client_list_create'),    
    path('<int:pk>/edit/', client_update, name='client_update'),
    path('<int:pk>/delete/', client_delete, name='client_delete'),
    #===================================================================================
    #OBRA
    path('<int:client_id>/obra/', obra_create_view, name='obra_create'),
    path('<int:pk>/obra/detail/', obra_list, name='obra_list'),
    path('<int:client_id>/obra/<int:pk>/update/', obra_update_view, name='obra_update'),
    path('<int:client_id>/obra/<int:pk>/delete/', obra_delete, name='obra_delete'), 
]