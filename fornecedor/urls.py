from django.urls import path

from .views import fornecedor_delete, fornecedor_list_create, fornecedor_update

app_name = 'fornecedor'

urlpatterns = [
    path('list/', fornecedor_list_create, name='fornecedor_list_create'),    
    path('<int:pk>/edit/', fornecedor_update, name='fornecedor_update'),
    path('<int:pk>/delete/', fornecedor_delete, name='fornecedor_delete'),
]    