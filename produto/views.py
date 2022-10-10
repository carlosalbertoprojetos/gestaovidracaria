from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import ProdutoForm
from .models import Categoria, Produto


success_url = _('product:products_list')

class CategoriaRegisterView(CreateView):
    model = Categoria
    template_name = 'product/category_register.html'
    fields = '__all__'
    success_message = 'Categoria cadastrada com sucesso!!!'
    success_url = success_url

categora_register = CategoriaRegisterView.as_view()


class ProdutoRegisterView(SuccessMessageMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'product/product_register.html'
    success_message = 'Produto cadastrado com sucesso!!!'
    success_url = success_url

produto_register = ProdutoRegisterView.as_view()


class ProdutoListView(ListView):
    model = Produto
    paginate_by = 4
    template_name = 'product/products_list.html'

produtos_list = ProdutoListView.as_view()


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'product/product_details.html'

produto_details = ProdutoDetailView.as_view()


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'product/product_update.html'
    success_message = 'Produto atualizado com sucesso!!!'
    success_url = success_url

produto_update = ProdutoUpdateView.as_view()
