# from django.shortcuts import redirect, render
# from .forms import MovimentoForm, ProdutoMovimento_factory


# def criar_movimento(request):
#     if request.method == 'GET':
#         form = MovimentoForm() 
#         formset = ProdutoMovimento_factory()

#         context = {
#             'form': form,
#             'form_order_products': formset
#         }
#         return render(request, 'order/order_create.html', context)

#     elif request.method == 'POST':
#         form = MovimentoForm(request.POST or None)
#         formset = ProdutoMovimento_factory(request.POST or None)

#         if form.is_valid():
#             form.save()
#             if formset.is_valid():
#                 formset.instance = form
#                 formset.save()
#                 return redirect('')

#         else:
#             context = {
#                 'form': form,
#                 'formset': formset
#             }
#             return render(request, 'order/order_create.html', context)