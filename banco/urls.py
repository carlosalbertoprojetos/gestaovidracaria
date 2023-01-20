from django.urls import path

from .views import banco_delete, banco_list_create, banco_update

app_name = 'banco'

urlpatterns = [
    path('list/', banco_list_create, name='banco_list_create'),    
    path('<int:pk>/edit/', banco_update, name='banco_update'),
    path('<int:pk>/delete/', banco_delete, name='banco_delete'),
]    