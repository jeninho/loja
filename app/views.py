"""
Definition of views.
"""

from django.shortcuts import render, redirect
from app.models import Produtos
from app.forms import FormProdutos

def index(request):
    """Renders the home page. """
    return render(request,
        'app/index.html')

def produtos(request):
    lista_itens = Produtos.objects.all()
    return render(request,
        'app/produtos.html',
        {'lista_item':lista_itens})

def adiciona(request):
    form = FormProdutos(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, 'app/adiciona.html', {'form':form})

def produto(request, nr_item):
    item = get_object_or_404(Produtos, pk=nr_item)
    form = FormProdutos(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "app/item.html", {'form': form})