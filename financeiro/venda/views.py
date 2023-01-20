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

from .forms import VendaForm, VendaPrestacaoForm, VendaProdutoForm, FormsetFactory_produto, FormsetFactory_prestacao, FormsetFactory_produto_up, FormsetFactory_prestacao_up, AnoForm
from .models import VendaProduto, Venda, VendaPrestacao


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
data = date.today()


#===============================================================================
#VENDA


def venda_create(request):
    template_name = 'venda/venda_create.html'

    if request.method == 'GET':
        form = VendaForm()
        pro_formset = FormsetFactory_produto()
        pre_formset = FormsetFactory_prestacao()

        context = {
            'form': form,
            'produto_formset': pro_formset,
            'prestacoes_formset': pre_formset
        }
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = VendaForm(request.POST)
        pro_formset = FormsetFactory_produto(request.POST)
        pre_formset = FormsetFactory_prestacao(request.POST)

        if form.is_valid() and pro_formset.is_valid() and pre_formset.is_valid():
            form = form.save()
            pro_formset.instance = form
            pro_formset.save()
            pre_formset.instance = form
            pre_formset.save()
            return redirect('venda:venda_list_create')
        
        else:
            context = {
                'form': form,
                'produto_formset': pro_formset,
                'prestacoes_formset': pre_formset
            }
            return render(request, template_name, context)


def venda_update2(request, pk):
    objeto = get_object_or_404(Venda, pk=pk)
    template_name = 'venda/venda_update2.html'

    if request.method == 'GET':
        form = VendaForm(instance=objeto)
        pro_formset = FormsetFactory_produto_up(instance=objeto)
        pre_formset = FormsetFactory_prestacao_up(instance=objeto)

        context = {
            'form': form,
            'produto_formset': pro_formset,
            'prestacoes_formset': pre_formset
        }
        return render(request, template_name, context)

    elif request.method == 'POST':
        form = VendaForm(request.POST, instance=objeto)
        pro_formset = FormsetFactory_produto_up(request.POST, instance=objeto)
        pre_formset = FormsetFactory_prestacao_up(request.POST, instance=objeto)

        if form.is_valid() and pro_formset.is_valid() and pre_formset.is_valid():
            form = form.save()
            pro_formset.instance = form
            pro_formset.save()
            pre_formset.instance = form
            pre_formset.save()
            return redirect('venda:venda_list_create')
        
        else:
            context = {
                'form': form,
                'produto_formset': pro_formset,
                'prestacoes_formset': pre_formset
            }
            return render(request, template_name, context)


class VendaListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Venda
    template_name = 'venda/venda_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(VendaListCreateView, self).get_context_data(**kwargs)
        context['form'] = VendaForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = VendaForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Venda criada com sucesso!!!')
            return redirect('venda:venda_list_create')
        else:
            return render(request, 'venda/venda_list_create.html', {'object':'object','form': form})

venda_list_create = VendaListCreateView.as_view()


class VendaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = 'venda/venda_update.html'
    success_message = 'Dados da venda alterados com sucesso!!!'
    success_url = _('venda:venda_list_create')

venda_update = VendaUpdateView.as_view()


class VendaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Venda
    template_name = 'venda/venda_delete.html'
    success_message = 'Venda deletada com sucesso!'
    success_url = _('venda:venda_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(VendaDeleteView, self).delete(request, *args, **kwargs)

venda_delete = VendaDeleteView.as_view()


#===============================================================================
#CRIA VENDA DE PRODUTOS

class VendaProdutoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = VendaProduto
    form_class = VendaProdutoForm
    template_name = 'venda/venda_produto_create.html'    
    
    def post(self, request, *args, **kwargs):

        form = VendaProdutoForm(request.POST or None)        
        venda_pk = self.kwargs.get('venda_id')        
        
        if form.is_valid():
            form = form.save(commit=False)
            form.venda_id = venda_pk
            form.save()
            messages.success(request, 'Venda do Produto criada com sucesso!!!')
            return HttpResponseRedirect("/venda/"+str(venda_pk)+"/produtos/detail")
        else:
            return render(request, 'venda/venda_produto_create.html', {'object':'object','form': form})

venda_produto_create_view = VendaProdutoCreateView.as_view()


#===============================================================================
# LISTA DE PRODUTOS VENDIDOS

def venda_produto_list(request, pk):
    context = {}
    form = VendaProdutoForm(request.POST or None)
    venda = Venda.objects.get(pk=pk)    
    venda_produto = VendaProduto.objects.filter(venda__id=pk)
      
    context = {
        'venda_produto':venda_produto,        
        'venda':venda,
        'form': form,            
    }
            
    if form.is_valid():
        form.save()
        messages.success(request, 'Venda do Produto criada com sucesso!!!')    
        return render(request, 'venda/venda_produto_list.html', context)
    else:         
         return render(request, 'venda/venda_produto_list.html', context)  


#=====================================================================================================
#ATUALIZAR VENDA E PRODUTOS

class VendaProdutoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):    
  
    model = VendaProduto
    form_class = VendaProdutoForm 
    template_name = 'venda/venda_produto_update.html'
    success_message = 'Venda dos Produtos alterada com sucesso!!!'   

    def post(self, request, **kwargs):        
        venda_pk = self.kwargs.get('venda_id')        
        pk = self.kwargs.get('pk')        
        
        obj = get_object_or_404(VendaProduto, pk=pk)
        form = VendaProdutoForm(request.POST or None, instance=obj)       
        if form.is_valid():
            form.save()
            messages.success(self.request,self.success_message)
            return HttpResponseRedirect("/venda/"+str(venda_pk)+"/produtos/detail")      

venda_produto_update_view = VendaProdutoUpdateView.as_view()


#=====================================================================================================
#DELETAR VENDA DE PRODUTOS  

def venda_produto_delete(request, **kwargs):
    
    context ={}
    pk = kwargs.get('pk') 
    
    obj = get_object_or_404(VendaProduto, pk = pk) 
 
    if request.method =="POST":
        venda_pk = kwargs.get('venda_id')
        # delete object
        obj.delete()
        messages.success(request, 'Venda dos Produtos deletada com sucesso!!!')
        return HttpResponseRedirect("/venda/"+str(venda_pk)+"/produtos/detail")
 
    return render(request, "venda/venda_produto_delete.html", context)


#===============================================================================
#CRIA PRESTACOES DA VENDA

class VendaPrestacaoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = VendaPrestacao
    form_class = VendaPrestacaoForm
    template_name = 'venda/venda_prestacao_create.html'    
    
    def post(self, request, *args, **kwargs):

        form = VendaPrestacaoForm(request.POST or None)        
        venda_pk = self.kwargs.get('venda_id')        
        
        if form.is_valid():
            form = form.save(commit=False)
            form.venda_id = venda_pk
            form.save()
            messages.success(request, 'Prestação criada com sucesso!!!')
            return HttpResponseRedirect("/venda/"+str(venda_pk)+"/prestacao/detail")
        else:
            return render(request, 'venda/venda_prestacao_create.html', {'object':'object','form': form})

venda_prestacao_create_view = VendaPrestacaoCreateView.as_view()


#===============================================================================
# LISTA DE PRESTACOES

def venda_prestacao_list(request, pk):
    context = {}
    form = VendaPrestacaoForm(request.POST or None)
    venda = Venda.objects.get(pk=pk)    
    venda_prestacao = VendaPrestacao.objects.filter(venda__id=pk)
      
    context = {
        'venda_prestacao':venda_prestacao,        
        'venda':venda,
        'form': form,            
    }
            
    if form.is_valid():
        form.save()
        messages.success(request, 'Prestação criada com sucesso!!!')    
        return render(request, 'venda/venda_prestacao_list.html', context)
    else:         
         return render(request, 'venda/venda_prestacao_list.html', context)  


#=====================================================================================================
#ATUALIZAR PRESTAÇÃO

class VendaPrestacaoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):    
  
    model = VendaPrestacao
    form_class = VendaPrestacaoForm 
    template_name = 'venda/venda_prestacao_update.html'
    success_message = 'Prestação alterada com sucesso!!!'   

    def post(self, request, **kwargs):        
        venda_pk = self.kwargs.get('venda_id')        
        pk = self.kwargs.get('pk')        
        
        obj = get_object_or_404(VendaPrestacao, pk=pk)
        form = VendaPrestacaoForm(request.POST or None, instance=obj)       
        if form.is_valid():
            form.save()
            messages.success(self.request,self.success_message)
            return HttpResponseRedirect("/venda/"+str(venda_pk)+"/prestacao/detail")      

venda_prestacao_update_view = VendaPrestacaoUpdateView.as_view()


#=====================================================================================================
#DELETAR PRESTAÇÃO  

def venda_prestacao_delete(request, **kwargs):
    
    context ={}
    pk = kwargs.get('pk') 
    
    obj = get_object_or_404(VendaPrestacao, pk = pk) 
 
    if request.method =="POST":
        venda_pk = kwargs.get('venda_id')
        # delete object
        obj.delete()
        messages.success(request, 'Pretação deletada com sucesso!!!')
        return HttpResponseRedirect("/venda/"+str(venda_pk)+"/prestacao/detail")
 
    return render(request, "venda/venda_prestacao_delete.html", context)


def contas_receber(request):
    venda = Venda.objects.all()
    # prest = VendaPrestacao.objects.filter(data_venc__month=data.month)
    prest = VendaPrestacao.objects.all()
    prestacoes = 0
    for p in prest:
        if p.venda.id == prest:
            prestacoes += 1
    mes = data.strftime('%B/%Y')
    template_name = 'venda/contas_receber.html'
    context = {
        'mes_atual': mes,
        'venda': venda,
        'prestacao': prest
    }
    return render(request, template_name, context)


#=====================================================================================================
#CONTAS A RECEBER

def ano_dropdown(request):
    select_anos = VendaPrestacao.objects.dates('data_venc', 'year')
    # prest = VendaPrestacao.objects.filter(data_venc__year=data.year).filter(data_venc__month=data.month)

    context = {
        # 'prestacao': prest,
        'form': AnoForm,
        'anos': select_anos,
    }
    return render(request, 'venda/menu_contas_areceber.html', context)


def meses_choices_ajax(request):
    ano = request.GET.get('ano')
    prest = VendaPrestacao.objects.filter(data_venc__year=ano)

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
        'prestacao':prest, 
        'meses': meses,
        'ano': ano
    }
    return render(request, 'venda/includes/_choices_meses.html', context)


def meses_prestacoes_ajax(request):
    ano = request.GET.get('ano')
    mes = request.GET.get('mes')
    prest = VendaPrestacao.objects.filter(data_venc__year=ano).filter(data_venc__month=mes)

    context = {
        'prestacao':prest, 
    }
    return render(request, 'venda/includes/_prestacoes.html', context)