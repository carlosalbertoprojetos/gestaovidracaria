# from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField('Categoria', max_length=255, unique=True)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class UnidadeMedida(models.Model):
    unidade = models.CharField('UM', max_length=10)
    
    def __str__(self):
        return self.unidade
    
    class Meta:
        verbose_name = "Unidade de Medida"
        verbose_name_plural = "Unidades de Medida"


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=255, unique=True)
    imagem = models.ImageField(
        'Imagem do produto', upload_to="produtos/%Y", blank=True)
    unimed = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE, blank=True, verbose_name='Unidade de medida')
    descricao = models.TextField('Descrição', blank=True)
    valor = models.DecimalField('Valor de Custo', max_digits=10, decimal_places=2, default=0)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2, default=0)
    disponivel = models.BooleanField('Disponível', default=True)
    estoque = models.IntegerField('Estoque', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def get_absolute_url_Detail(self):
        return reverse('product:product_detail', args=[self.pk])
    
    def get_absolute_url_Update(self):
        return reverse('product:product_update', args=[self.pk])
    
    def get_absolute_url_Delete(self):
        return reverse('product:product_delete', args=[self.pk])
    
    def __str__(self):
        return self.nome


# @receiver(post_save, sender=Produto)
# def inventory_delete(sender, instance, **kwargs):
#     produto = Produto.objects.filter(pk=instance.produto_id)
#     for p in produto:
#         p.estoque -= instance.quantidade
#         p.save()

#     movimento = Movimento.objects.filter(pk=instance.movimento_id)
#     for o in movimento:
#         print('ORDER', o)
#     # order.total = sum
#     # order.save()

# @receiver(post_delete, sender=Produto)
# def inventory_insert(sender, instance, **kwargs):
#     produto = Produto.objects.filter(pk=instance.produto_id)
#     for p in produto:
#         p.estoque += instance.quantidade
#         p.save()