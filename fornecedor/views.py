from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import FornecedorForm
from .models import Fornecedor


class FornecedorListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Fornecedor
    template_name = 'fornecedor/fornecedor_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(FornecedorListCreateView, self).get_context_data(**kwargs)
        context['form'] = FornecedorForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = FornecedorForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor criado com sucesso!!!')
            return redirect('fornecedor:fornecedor_list_create')
        else:
            return render(request, 'fornecedor/fornecedor_list_create.html', {'object':'object','form': form})

fornecedor_list_create = FornecedorListCreateView.as_view()


class FornecedorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedor/fornecedor_update.html'
    success_message = 'Dados do fornecedor alterados com sucesso!!!'
    success_url = _('fornecedor:fornecedor_list_create')

fornecedor_update = FornecedorUpdateView.as_view()


class FornecedorDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Fornecedor
    template_name = 'fornecedor/fornecedor_delete.html'
    success_message = 'Fornecedor deletado com sucesso!'
    success_url = _('fornecedor:fornecedor_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(FornecedorDeleteView, self).delete(request, *args, **kwargs)

fornecedor_delete = FornecedorDeleteView.as_view()
