from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import BancoForm
from .models import Banco


class BancoListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Banco
    template_name = 'banco/banco_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(BancoListCreateView, self).get_context_data(**kwargs)
        context['form'] = BancoForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = BancoForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Banco criado com sucesso!!!')
            return redirect('banco:banco_list_create')
        else:
            return render(request, 'banco/banco_list_create.html', {'object':'object','form': form})

banco_list_create = BancoListCreateView.as_view()

class BancoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Banco
    form_class = BancoForm
    template_name = 'banco/banco_update.html'
    success_message = 'Dados do banco alterados com sucesso!!!'
    success_url = _('banco:banco_list_create')

banco_update = BancoUpdateView.as_view()


class BancoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Banco
    template_name = 'banco/banco_delete.html'
    success_message = 'Banco deletado com sucesso!'
    success_url = _('banco:banco_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(BancoDeleteView, self).delete(request, *args, **kwargs)

banco_delete = BancoDeleteView.as_view()
