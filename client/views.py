from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .forms import ClientForm, ObraForm
from .models import Client, Obra


#===============================================================================
#Cria Obra
class ObraCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Obra
    form_class = ObraForm
    template_name = 'client/obra_create.html'    
    
    def post(self, request, *args, **kwargs):

        form = ObraForm(request.POST or None)        
        client_pk = self.kwargs.get('client_id')
        
        #obra = Obra.objects.filter(cliente=client_pk)               
        #cliente = Client.objects.get(id=client_pk)
        #print(event)
        #print(season)
        
        #for e in Event.objects.filter(season=pk):           
        #   date_init_list = e.date_init #.strftime("%-d/%-m/%Y")           
        #   date_fin_list = e.date_fin #.strftime("%-d/%-m/%Y")
        #   delta = date_fin_list - date_init_list       
        
        if form.is_valid():
            form = form.save(commit=False)
            form.cliente_id = client_pk
            form.save()
            messages.success(request, 'Obra criada com sucesso!!!')
            return HttpResponseRedirect("/client/"+str(client_pk)+"/obra/detail")
        else:
            return render(request, 'client/obra_create.html', {'object':'object','form': form})

obra_create_view = ObraCreateView.as_view()

#===============================================================================
# Listar Obras

def obra_list(request, pk):
    context = {}
    form = ObraForm(request.POST or None)
    cliente = Client.objects.get(pk=pk)    
    obra = Obra.objects.filter(cliente__id=pk)
      
    context = {
        'obra':obra,        
        'cliente': cliente,
        'form': form,            
    }
            
    if form.is_valid():
        form.save()
        messages.success(request, 'Obra criada com sucesso!!!')    
        return render(request, 'client/obra_list.html', context)
    else:         
         return render(request, 'client/obra_list.html', context)  

#=====================================================================================================
#Atualisar Obra

class ObraUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):    
  
    model = Obra
    form_class = ObraForm 
    template_name = 'client/obra_update.html'
    success_message = 'Obra alterado com sucesso!!!'   

    def post(self, request, **kwargs):        
        cliente_pk = self.kwargs.get('client_id')        
        pk = self.kwargs.get('pk')        
        
        obj = get_object_or_404(Obra, pk=pk)
        form = ObraForm(request.POST or None, instance=obj)       
        if form.is_valid():
            form.save()
            messages.success(self.request,self.success_message)
            return HttpResponseRedirect("/client/"+str(cliente_pk)+"/obra/detail")      

obra_update_view = ObraUpdateView.as_view()

#=====================================================================================================
#Deletar Obra  

def obra_delete(request, **kwargs):
    
    context ={}
    pk = kwargs.get('pk')
    client_id = kwargs.get('client_id') 
    nome = Client.objects.filter(id=client_id)    
        
    context = {
                
        'nome': nome[0],                   
    } 
    
    obj = get_object_or_404(Obra, pk = pk) 
 
    if request.method =="POST":
        client_pk = kwargs.get('client_id')
        # delete object
        obj.delete()
        messages.success(request, 'Obra deletada com sucesso!!!')
        return HttpResponseRedirect("/client/"+str(client_pk)+"/obra/detail")
 
    return render(request, "client/obra_delete.html", context)

#===============================================================================
#CLIENTE
class ClientListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Client
    template_name = 'client/client_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(ClientListCreateView, self).get_context_data(**kwargs)
        context['form'] = ClientForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente criado com sucesso!!!')
            return redirect('client:client_list_create')
        else:
            return render(request, 'client/client_list_create.html', {'object':'object','form': form})

client_list_create = ClientListCreateView.as_view()


class ClientUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_update.html'
    success_message = 'Dados do cliente alterados com sucesso!!!'
    success_url = _('client:client_list_create')

client_update = ClientUpdateView.as_view()


class ClientDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Client
    template_name = 'client/client_delete.html'
    success_message = 'Cliente deletado com sucesso!'
    success_url = _('client:client_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(ClientDeleteView, self).delete(request, *args, **kwargs)

client_delete = ClientDeleteView.as_view()
