from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from datetime import date
import locale

from .forms import CompraForm, CompraPrestacaoForm, CompraProdutoForm, FormsetFactory_produto, FormsetFactory_produto_up, FormsetFactory_prestacao, FormsetFactory_prestacao_up, AnoForm
from .models import Compra, CompraProduto, CompraPrestacao


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
data = date.today()

#===============================================================================
#COMPRA

def lista_geral(request):
    objeto = Compra.objects.all()
    # produto = CompraProduto.objects.all()
    # prestacao = CompraPrestacao.objects.all()
    
    template_name = 'compra/compra_lista.html'
    context = {
        'object_list': objeto,
        
    }
    return render(request, template_name, context)


def compra_create(request):
    template_name = 'compra/compra_create.html'

    if request.method == 'GET':
        form = CompraForm()
        pro_formset = FormsetFactory_produto()
        pre_formset = FormsetFactory_prestacao()

        context = {
            'form': form,
            'produto_formset': pro_formset,
            'prestacoes_formset': pre_formset
        }
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = CompraForm(request.POST)
        pro_formset = FormsetFactory_produto(request.POST)
        pre_formset = FormsetFactory_prestacao(request.POST)

        if form.is_valid() and pro_formset.is_valid() and pre_formset.is_valid():
            form = form.save()
            pro_formset.instance = form
            pro_formset.save()
            pre_formset.instance = form
            pre_formset.save()
            return redirect('compra:compra_list_create')
        
        else:
            context = {
                'form': form,
                'produto_formset': pro_formset,
                'prestacoes_formset': pre_formset
            }
            return render(request, template_name, context)


def compra_update2(request, pk):
    objeto = get_object_or_404(Compra, pk=pk)
    template_name = 'compra/compra_update2.html'

    if request.method == 'GET':
        form = CompraForm(instance=objeto)
        pro_formset = FormsetFactory_produto_up(instance=objeto)
        pre_formset = FormsetFactory_prestacao_up(instance=objeto)
        context = {
            'form': form,
            'produto_formset': pro_formset,
            'prestacoes_formset': pre_formset
        }
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = CompraForm(request.POST, instance=objeto)
        pro_formset = FormsetFactory_produto_up(request.POST, instance=objeto)
        pre_formset = FormsetFactory_prestacao_up(request.POST, instance=objeto)

        if form.is_valid() and pro_formset.is_valid() and pre_formset.is_valid():
            form = form.save()
            pro_formset.instance = form
            pro_formset.save()
            pre_formset.instance = form
            pre_formset.save()
            return redirect('compra:compra_list_create')
        
        else:
            context = {
                'form': form,
                'produto_formset': pro_formset,
                'prestacoes_formset': pre_formset
            }
            return render(request, template_name, context)



class CompraListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Compra
    template_name = 'compra/compra_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(CompraListCreateView, self).get_context_data(**kwargs)
        context['form'] = CompraForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = CompraForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Compra criada com sucesso!!!')
            return redirect('compra:compra_list_create')
        else:
            return render(request, 'compra/compra_list_create.html', {'object':'object','form': form})

compra_list_create = CompraListCreateView.as_view()


class CompraUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compra/compra_update.html'
    success_message = 'Dados da compra alterados com sucesso!!!'
    success_url = _('compra:compra_list_create')

compra_update = CompraUpdateView.as_view()


class CompraDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Compra
    template_name = 'compra/compra_delete.html'
    success_message = 'Compra deletada com sucesso!'
    success_url = _('compra:compra_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(CompraDeleteView, self).delete(request, *args, **kwargs)

compra_delete = CompraDeleteView.as_view()


#===============================================================================
#CRIA COMPRA PRODUTOS

class CompraProdutoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CompraProduto
    form_class = CompraProdutoForm
    template_name = 'compra/compra_produto_create.html'
    # success_url = '/dashboard/'

    def post(self, request, *args, **kwargs):
        form = CompraProdutoForm(request.POST or None)
        compra_pk = self.kwargs.get('compra_id')

        if form.is_valid():
            form = form.save(commit=False)
            form.compra_id = compra_pk
            form.save()
            messages.success(request, 'Compra do Produto criada com sucesso!!!')
            return HttpResponseRedirect("/compra/"+str(compra_pk)+"/produtos/detail")
        else:
            return render(request, 'compra/compra_produto_create.html', {'object':'object','form': form})

compra_produto_create_view = CompraProdutoCreateView.as_view()


#===============================================================================
# LISTA DE COMPRAS DE PRODUTOS

def compra_produto_list(request, pk):
    form = CompraProdutoForm(request.POST or None)
    compra = Compra.objects.get(pk=pk)    
    compra_produto = CompraProduto.objects.filter(compra__id=pk)
      
    context = {
        'compra_produto':compra_produto,        
        'compra':compra,
        'form': form,            
    }
            
    if form.is_valid():
        form.save()
        messages.success(request, 'Compra do Produto criada com sucesso!!!')    
        return render(request, 'compra/compra_produto_list.html', context)
    else:         
         return render(request, 'compra/compra_produto_list.html', context)  


#=====================================================================================================
#ATUALIZAR COMPRA E PRODUTOS

class CompraProdutoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):    
  
    model = CompraProduto
    form_class = CompraProdutoForm 
    template_name = 'compra/compra_produto_update.html'
    success_message = 'Compra dos Produtos alterada com sucesso!!!'   

    def post(self, request, **kwargs):        
        compra_pk = self.kwargs.get('compra_id')        
        pk = self.kwargs.get('pk')        
        
        obj = get_object_or_404(CompraProduto, pk=pk)
        form = CompraProdutoForm(request.POST or None, instance=obj)       
        if form.is_valid():
            form.save()
            messages.success(self.request,self.success_message)
            return HttpResponseRedirect("/compra/"+str(compra_pk)+"/produtos/detail")      

compra_produto_update_view = CompraProdutoUpdateView.as_view()


#=====================================================================================================
#DELETAR COMPRA DE PRODUTOS  

def compra_produto_delete(request, **kwargs):
    
    context ={}
    pk = kwargs.get('pk') 
    
    obj = get_object_or_404(CompraProduto, pk = pk) 
 
    if request.method =="POST":
        compra_pk = kwargs.get('compra_id')
        # delete object
        obj.delete()
        messages.success(request, 'Compra dos Produtos deletada com sucesso!!!')
        return HttpResponseRedirect("/compra/"+str(compra_pk)+"/produtos/detail")
 
    return render(request, "compra/compra_produto_delete.html", context)


#===============================================================================
#CRIA PRESTACOES DA COMPRA

class CompraPrestacaoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CompraPrestacao
    form_class = CompraPrestacaoForm
    template_name = 'compra/compra_prestacao_create.html'    
    
    def post(self, request, *args, **kwargs):

        form = CompraPrestacaoForm(request.POST or None)        
        compra_pk = self.kwargs.get('compra_id')        
        
        if form.is_valid():
            form = form.save(commit=False)
            form.compra_id = compra_pk
            form.save()
            messages.success(request, 'Prestação criada com sucesso!!!')
            return HttpResponseRedirect("/compra/"+str(compra_pk)+"/prestacao/detail")
        else:
            return render(request, 'compra/compra_prestacao_create.html', {'object':'object','form': form})

compra_prestacao_create_view = CompraPrestacaoCreateView.as_view()


#===============================================================================
# LISTA DE PRESTACOES

def compra_prestacao_list(request, pk):
    context = {}
    form = CompraPrestacaoForm(request.POST or None)
    compra = Compra.objects.get(pk=pk)    
    compra_prestacao = CompraPrestacao.objects.filter(compra__id=pk)
      
    context = {
        'compra_prestacao':compra_prestacao,        
        'compra':compra,
        'form': form,            
    }
            
    if form.is_valid():
        form.save()
        messages.success(request, 'Prestação criada com sucesso!!!')    
        return render(request, 'compra/compra_prestacao_list.html', context)
    else:         
         return render(request, 'compra/compra_prestacao_list.html', context)  


#=====================================================================================================
#ATUALIZAR PRESTAÇÃO

class CompraPrestacaoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):    
  
    model = CompraPrestacao
    form_class = CompraPrestacaoForm 
    template_name = 'compra/compra_prestacao_update.html'
    success_message = 'Prestação alterada com sucesso!!!'   

    def post(self, request, **kwargs):        
        compra_pk = self.kwargs.get('compra_id')        
        pk = self.kwargs.get('pk')        
        
        obj = get_object_or_404(CompraPrestacao, pk=pk)
        form = CompraPrestacaoForm(request.POST or None, instance=obj)       
        if form.is_valid():
            form.save()
            messages.success(self.request,self.success_message)
            return HttpResponseRedirect("/compra/"+str(compra_pk)+"/prestacao/detail")      

compra_prestacao_update_view = CompraPrestacaoUpdateView.as_view()


#=====================================================================================================
#DELETAR PRESTAÇÃO  

def compra_prestacao_delete(request, **kwargs):
    context ={}
    pk = kwargs.get('pk') 

    obj = get_object_or_404(CompraPrestacao, pk = pk) 

    if request.method =="POST":
        compra_pk = kwargs.get('compra_id')
        # delete object
        obj.delete()
        messages.success(request, 'Pretação deletada com sucesso!!!')
        return HttpResponseRedirect("/compra/"+str(compra_pk)+"/prestacao/detail")

    return render(request, "compra/compra_prestacao_delete.html", context)


#=====================================================================================================
#CONTAS A PAGAR

def ano_dropdown(request):
    select_anos = CompraPrestacao.objects.dates('data_venc', 'year')
    # prest = CompraPrestacao.objects.filter(data_venc__year=data.year).filter(data_venc__month=data.month)

    context = {
        # 'prestacao': prest,
        'form': AnoForm,
        'anos': select_anos,
    }
    return render(request, 'compra/menu_contas_apagar.html', context)


def meses_choices_ajax(request):
    ano = request.GET.get('ano')
    prest = CompraPrestacao.objects.filter(data_venc__year=ano)

    # filtra os meses
    dict = {}
    for p in prest:
        if not p.data_venc.strftime('%B') in dict:
            i = int(p.data_venc.month)
            m = p.data_venc.strftime('%B')
            dict[i] = m
    # ordena os meses
    meses = {}
    for i in sorted(dict):
        n = i
        m = dict[i]
        meses[n] = m

    context = {
        'prestacao': prest, 
        'meses': meses,
        'ano': ano
    }
    return render(request, 'compra/includes/_choices_meses.html', context)


def meses_prestacoes_ajax(request):
    ano = request.GET.get('ano')
    mes = request.GET.get('mes')
    prest = CompraPrestacao.objects.filter(data_venc__year=ano).filter(data_venc__month=mes)

    context = {
        'prestacao': prest, 
    }
    return render(request, 'compra/includes/_prestacoes.html', context)