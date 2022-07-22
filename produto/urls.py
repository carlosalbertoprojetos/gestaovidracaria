from django.urls import path

from .views import (categora_register, 
                    produto_register, produtos_list,
                    produto_details, produto_update, )


app_name = 'produto'


urlpatterns = [
    path('category/', categora_register, name="categora_register"),
    
    path('register/', produto_register, name='produto_register'),
    path('list/', produtos_list, name='produtos_list'),
    path('<int:pk>/detalhes/', produto_details, name='produto_details'),
    path('<int:pk>/atualizar/', produto_update, name='produto_update'),
]
