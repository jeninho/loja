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

def addProduto(request):
    if request.method == 'POST':
        form = FormProdutos(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = FormProdutos()

    return render(request, "addproduto.html", {'form':form})
