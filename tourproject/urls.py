"""tourproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),    
    path('user/', include('user.urls'), name='user'),
    #path('company/', include('company.urls'), name='company'),

    #path('trip/', include('trip.urls'), name='company'),
    #path('destiny/', include('destiny.urls'), name='destiny'),
    #path('season/', include('season.urls'), name='season'),

    path('client/', include('client.urls'), name='client'),
    path('funcionario/', include('funcionario.urls'), name='funcionario'),
    path('banco/', include('banco.urls'), name='banco'),
    # path('cheque/', include('cheque.urls'), name='cheque'),
    path('fornecedor/', include('fornecedor.urls'), name='fornecedor'),
    path('produto/', include('produto.urls'), name='produto'),
    # path('mensalgeral/', include('mensalgeral.urls'), name='mensalgeral'),
    # path('compra/', include('compra.urls'), name='compra'),
    # path('venda/', include('venda.urls'), name='venda'),
    # path('caixadia/', include('caixadia.urls'), name='caixadia'),
    path('estoquefisico/', include('estoquefisico.urls'), name='estoquefisico'),    
    #path('transport/', include('transport.urls'), name='transport'),

    path('accounts/', include('allauth.urls')),

    path('admin/', admin.site.urls),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
