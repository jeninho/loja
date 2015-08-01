"""
Definition of forms.
"""

from django import forms
from app.models import Produtos

class FormProdutos(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ('nome', 'valor', 'descricao')