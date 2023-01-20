import pdb
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView


from .forms import EstoqueFisicoForm
from .models import EstoqueFisico, Produto

#===============================================================================
#Produto

class EstoqueFisicoListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = EstoqueFisico
    template_name = 'estoquefisico/estoquefisico_list_create.html'   
    
    def get_context_data(self, **kwargs):
        context = super(EstoqueFisicoListCreateView, self).get_context_data(**kwargs)
        context['form'] = EstoqueFisicoForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = EstoqueFisicoForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado no estoque com sucesso!!!')
            return redirect('estoquefisico:estoquefisico_list_create')
        else:
            return render(request, 'estoquefisico/estoquefisico_list_create.html', {'object':'object','form': form})

estoquefisico_list_create = EstoqueFisicoListCreateView.as_view()

class EstoqueFisicoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = EstoqueFisico
    form_class = EstoqueFisicoForm
    template_name = 'estoquefisico/estoquefisico_update.html'
    success_message = 'Dados do estoque alterados com sucesso!!!'
    success_url = _('estoquefisico:estoquefisico_list_create')

estoquefisico_update = EstoqueFisicoUpdateView.as_view()

class EstoqueFisicoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = EstoqueFisico
    template_name = 'estoquefisico/estoquefisico_delete.html'
    success_message = 'Produto no estoque fisico deletado com sucesso!'
    success_url = _('estoquefisico:estoquefisico_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(EstoqueFisicoDeleteView, self).delete(request, *args, **kwargs)

estoquefisico_delete = EstoqueFisicoDeleteView.as_view()

#===============================================================================