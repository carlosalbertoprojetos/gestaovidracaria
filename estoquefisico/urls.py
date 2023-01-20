from django.urls import path

from .views import (
                    estoquefisico_delete, estoquefisico_list_create, estoquefisico_update
                    )
 

app_name = 'estoquefisico'

urlpatterns = [

    #PRODUTOS
    path('list/', estoquefisico_list_create, name='estoquefisico_list_create'),    
    path('<int:pk>/edit/', estoquefisico_update, name='estoquefisico_update'),
    path('<int:pk>/delete/', estoquefisico_delete, name='estoquefisico_delete'),
   
]