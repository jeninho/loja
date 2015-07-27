"""
Definition of forms.
"""

from django import forms
from app.models import Produtos

class FormProdutos(forms.ModelForm):
    #data = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
     #   input_formats=['%d/%m/%Y','%d/%m/%y'])

    class Meta:
        model = Produtos
        fields = ('nome', 'valor', 'descricao')