from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required


from .forms import ProdutoForm, TributosForm, CategoriaForm, UnidadeMedidaForm, FormsetFactory

from .models import Produto, Tributos, UnidadeMedida, Categoria


#===============================================================================
#Cria Tributo
class TributoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tributos
    form_class = TributosForm
    template_name = 'produto/tributo_create.html'    
    
    def post(self, request, *args, **kwargs):

        form = TributosForm(request.POST or None)        
        produto_pk = self.kwargs.get('produto_id')        
             
        
        if form.is_valid():
            form = form.save(commit=False)
            form.produto_id = produto_pk
            form.save()
            messages.success(request, 'Tributos criados com sucesso!!!')
            return HttpResponseRedirect("/produto/"+str(produto_pk)+"/tributo/detail")
        else:
            return render(request, 'produto/tributo_create.html', {'object':'object','form': form})

tributo_create_view = TributoCreateView.as_view()

#===============================================================================
# Listar Tributos

def tributo_list(request, pk):
    context = {}
    form = TributosForm(request.POST or None)
    #id = Produto.objects.filter(pk=pk).values_list('id')
    produto = Produto.objects.get(pk=pk)
    tributo = Tributos.objects.filter(produto__id=pk)
     
    context = {
        'pk': id,
        'tributo':tributo,        
        'produto':produto,
        'form': form,            
    }
             
    if form.is_valid():
        form.save()
        messages.success(request, 'Tributos criados com sucesso!!!')    
        return render(request, 'produto/tributo_list.html', context)
    else:         
         return render(request, 'produto/tributo_list.html', context)  

#=====================================================================================================
#Atualisar Tributos

class TributoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):    
  
    model = Tributos
    form_class = TributosForm 
    template_name = 'produto/tributo_update.html'
    success_message = 'Tributos alterados com sucesso!!!'   

    def post(self, request, **kwargs):        
        produto_pk = self.kwargs.get('produto_id')        
        pk = self.kwargs.get('pk')        
        
        obj = get_object_or_404(Tributos, pk=pk)
        form = TributosForm(request.POST or None, instance=obj)       
        if form.is_valid():
            form.save()
            messages.success(self.request,self.success_message)
            return HttpResponseRedirect("/produto/"+str(produto_pk)+"/tributo/detail")      

tributo_update_view = TributoUpdateView.as_view()

#=====================================================================================================
#Deletar Tributos  

def tributo_delete(request, **kwargs):
    
    context ={}
    pk = kwargs.get('pk') 
    
    obj = get_object_or_404(Tributos, pk = pk) 
 
    if request.method =="POST":
        produto_pk = kwargs.get('produto_id')
        # delete object
        obj.delete()
        messages.success(request, 'Tributos deletados com sucesso!!!')
        return HttpResponseRedirect("/produto/"+str(produto_pk)+"/tributo/detail")
 
    return render(request, "produto/tributo_delete.html", context)

#===============================================================================
#TABELA DE CÁLCULOS

def tabela_list(request, **kwargs):
    
    context = {}
    #form = TributosForm(request.POST or None)
    
    pk = kwargs.get('produto_id')
    produto = Produto.objects.get(pk=pk)
    tributo = kwargs.get('pk')
    
    context = {                
        'produto':produto,
        #'form': form,            
    }
    
    return render(request, 'produto/tabelacalculos_list.html', context)
    #return render(request,"/produto/"+str(produto)+"/tributo/"+str(tributo)+"/detail/tabela/tabelacalculos_list.html")         
    #if form.is_valid():
    #    form.save()
    #    messages.success(request, 'Tabela de cálculos criada com sucesso!!!')    
    #    return render(request, 'produto/tabelacalculos_list.html', context)
    #else:         
    #     return render(request, 'produto/tabelacalculos_list.html', context)
    
    '''
    context = {}
    form = TributosForm(request.POST or None)
    produto = Produto.objects.get(pk=pk)    
    tributo = Tributos.objects.filter(produto__id=pk)
      
    context = {
        'tributo':tributo,        
        'produto':produto,
        'form': form,            
    }
             
    if form.is_valid():
        form.save()
        messages.success(request, 'Tributos criados com sucesso!!!')    
        return render(request, 'produto/tributo_list.html', context)
    else:         
         return render(request, 'produto/tributo_list.html', context)
    '''
    
#===============================================================================
#Produto


@login_required
def produto_list_create(request):
    objeto = Produto.objects.all()
    template_name = 'produto/produto_list_create.html'
    
    if request.method == 'GET':
        form = ProdutoForm()
        # lanc_factory = inlineformset_factory(Produto, Tributos, form=TributosForm, extra=1)
        formset = FormsetFactory()
        context = {
            'object_list': objeto,
            'form': form,
            'formset': formset,
        }
        return render(request, 'produto/produto_list_create.html', context)
    
    elif request.method == 'POST':
        form = ProdutoForm(request.POST)
        # lanc_factory = inlineformset_factory(Produto, Tributos, form=TributosForm, extra=1)
        formset = FormsetFactory(request.POST)

        if form.is_valid() and formset.is_valid():
            conta = form.save()
            formset.instance = conta
            formset.save()
            return redirect(reverse('produto:produto_list_create'))

        else:
            context = {
                'object_list': objeto,
                'form': form,
                'formset': formset,
            }
            return render(request, template_name, context)


@login_required
def produto_update(request, pk):
    objeto = get_object_or_404(Produto, pk=pk)
    template_name = 'produto/produto_update.html'
    
    if request.method == 'GET':
        form = ProdutoForm(instance=objeto)
        formset = FormsetFactory(instance=objeto)
        context = {
            'object_list': objeto,
            'form': form,
            'formset': formset,
        }
        return render(request, 'produto/produto_update.html', context)
    
    elif request.method == 'POST':
        form = ProdutoForm(request.POST, instance=objeto)
        formset = FormsetFactory(request.POST, instance=objeto)

        if form.is_valid() and formset.is_valid():
            conta = form.save()
            formset.instance = conta
            formset.save()
            return redirect(reverse('produto:produto_list_create'))

        else:
            context = {
                'object_list': objeto,
                'form': form,
                'formset': formset,
            }
            return render(request, template_name, context)

# class ProdutoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = Produto
#     form_class = ProdutoForm
#     template_name = 'produto/produto_update.html'
#     success_message = 'Dados do produto alterados com sucesso!!!'
#     success_url = _('produto:produto_list_create')

# produto_update = ProdutoUpdateView.as_view()

class ProdutoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Produto
    template_name = 'produto/produto_delete.html'
    success_message = 'Produto deletado com sucesso!'
    success_url = _('produto:produto_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(ProdutoDeleteView, self).delete(request, *args, **kwargs)

produto_delete = ProdutoDeleteView.as_view()

#===============================================================================
#Categoria

class CategoriaListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Categoria
    template_name = 'produto/categoria_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategoriaListCreateView, self).get_context_data(**kwargs)
        context['form'] = CategoriaForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = CategoriaForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria criada com sucesso!!!')
            return redirect('produto:categoria_list_create')
        else:
            return render(request, 'produto/categoria_list_create.html', {'object':'object','form': form})

categoria_list_create = CategoriaListCreateView.as_view()

class CategoriaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'produto/categoria_update.html'
    success_message = 'Dados da categoria alterados com sucesso!!!'
    success_url = _('produto:categoria_list_create')

categoria_update = CategoriaUpdateView.as_view()

class CategoriaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Categoria
    template_name = 'produto/categoria_delete.html'
    success_message = 'Categoria deletado com sucesso!'
    success_url = _('produto:categoria_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(ProdutoDeleteView, self).delete(request, *args, **kwargs)

categoria_delete = CategoriaDeleteView.as_view()

#===============================================================================
#Unidade de Medida

class UnimedListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = UnidadeMedida
    template_name = 'produto/unimed_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(UnimedListCreateView, self).get_context_data(**kwargs)
        context['form'] = UnidadeMedidaForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = UnidadeMedidaForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Unidade criada com sucesso!!!')
            return redirect('produto:unimed_list_create')
        else:
            return render(request, 'produto/unimed_list_create.html', {'object':'object','form': form})

unimed_list_create = UnimedListCreateView.as_view()

class UnimedUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UnidadeMedida
    form_class = UnidadeMedidaForm
    template_name = 'produto/unimed_update.html'
    success_message = 'Dados da unidade alterados com sucesso!!!'
    success_url = _('produto:unimed_list_create')

unimed_update = UnimedUpdateView.as_view()

class UnimedDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = UnidadeMedida
    template_name = 'produto/unimed_delete.html'
    success_message = 'Unidade deletado com sucesso!'
    success_url = _('produto:unimed_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(UnimedDeleteView, self).delete(request, *args, **kwargs)

unimed_delete = UnimedDeleteView.as_view()


def calculos_tritubos_lista(request):
    tributos = Tributos.objects.all()
    template_name = 'produto/produto_lista.html'
    context = {
        'tritubos':tributos        
    }    
    return render(request, template_name, context)