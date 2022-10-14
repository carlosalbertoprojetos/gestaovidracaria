from django.urls import path

# from .views import destiny_delete, destiny_list_create, destiny_update
from . import views

app_name = 'conta'

urlpatterns = [
    path('', views.conta_view, name='conta_view')
    # path('list/', conta_create, name='conta_create'),
    # path('<int:pk>/edit/', conta_edit, name='edit_create'),
    # path('<int:pk>/delete/', conta_delete, name='conta_delete'),
]