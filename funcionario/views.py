from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .forms import FuncionarioForm, FilhoForm
from .models import Funcionario, Filho


#===============================================================================
#Cria Filho
class FilhoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Filho
    form_class = FilhoForm
    template_name = 'funcionario/filho_create.html'    
    
    def post(self, request, *args, **kwargs):

        form = FilhoForm(request.POST or None)        
        funcionario_pk = self.kwargs.get('funcionario_id')             
        
        if form.is_valid():
            form = form.save(commit=False)
            form.funcionario_id = funcionario_pk
            form.save()
            messages.success(request, 'Filho criada com sucesso!!!')
            return HttpResponseRedirect("/funcionario/"+str(funcionario_pk)+"/filho/detail")
        else:
            return render(request, 'funcionario/filho_create.html', {'object':'object','form': form})

filho_create_view = FilhoCreateView.as_view()

#===============================================================================
# Listar Obras

def filho_list(request, pk):
    context = {}
    form = FilhoForm(request.POST or None)
    funcionario = Funcionario.objects.get(pk=pk)    
    filho = Filho.objects.filter(funcionario__id=pk)
      
    context = {
        'filho':filho,        
        'funcionario':funcionario,
        'form': form,            
    }
           
    if form.is_valid():
        form.save()
        messages.success(request, 'Filho criada com sucesso!!!')    
        return render(request, 'funcionario/filho_list.html', context)
    else:         
         return render(request, 'funcionario/filho_list.html', context)  

#=====================================================================================================
#Atualisar Filho

class FilhoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):    
  
    model = Filho
    form_class = FilhoForm 
    template_name = 'funcionario/filho_update.html'
    success_message = 'Filho alterado com sucesso!!!'   

    def post(self, request, **kwargs):        
        funcionario_pk = self.kwargs.get('funcionario_id')        
        pk = self.kwargs.get('pk')        
        
        obj = get_object_or_404(Filho, pk=pk)
        form = FilhoForm(request.POST or None, instance=obj)       
        if form.is_valid():
            form.save()
            messages.success(self.request,self.success_message)
            return HttpResponseRedirect("/funcionario/"+str(funcionario_pk)+"/filho/detail")      

filho_update_view = FilhoUpdateView.as_view()

#=====================================================================================================
#Deletar Filho  

def filho_delete(request, **kwargs):
    
    context ={}
    pk = kwargs.get('pk')

    funcionario_id = kwargs.get('funcionario_id') 
    nome = Funcionario.objects.filter(id=funcionario_id)    
        
    context = {
                
        'nome': nome[0],                   
    }  
    
    obj = get_object_or_404(Filho, pk = pk) 
 
    if request.method =="POST":
        funcionario_pk = kwargs.get('funcionario_id')
        # delete object
        obj.delete()
        messages.success(request, 'Filho deletado com sucesso!!!')
        return HttpResponseRedirect("/funcionario/"+str(funcionario_pk)+"/filho/detail")
 
    return render(request, "funcionario/filho_delete.html", context)

#===============================================================================
#FUNCIONARIO

class FuncionarioListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Funcionario
    template_name = 'funcionario/funcionario_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(FuncionarioListCreateView, self).get_context_data(**kwargs)
        context['form'] = FuncionarioForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = FuncionarioForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionario criado com sucesso!!!')
            return redirect('funcionario:funcionario_list_create')
        else:
            return render(request, 'funcionario/funcionario_list_create.html', {'object':'object','form': form})

funcionario_list_create = FuncionarioListCreateView.as_view()


class FuncionarioUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionario/funcionario_update.html'
    success_message = 'Dados do funcionário alterados com sucesso!!!'
    success_url = _('funcionario:funcionario_list_create')

funcionario_update = FuncionarioUpdateView.as_view()


class FuncionarioDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Funcionario
    template_name = 'funcionario/funcionario_delete.html'
    success_message = 'Funcionário deletado com sucesso!'
    success_url = _('funcionario:funcionario_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(FuncionarioDeleteView, self).delete(request, *args, **kwargs)

funcionario_delete = FuncionarioDeleteView.as_view()
