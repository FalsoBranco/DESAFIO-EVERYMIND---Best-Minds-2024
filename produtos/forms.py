from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome",  "descricao", "preco"]
        labels = {"nome": "Produto"}
        help_texts = {
            "nome": "Nome do produto que deseja adicionar",
           
            "descricao": "Uma breve descrição do produto",
            "preco": "Preço do produto",

        }
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "input",
                    "type": "text",
                    "placeholder": "Nome do produto",
                },
            ),
        
            "descricao": forms.Textarea(attrs={"class": "textarea"}),
            "preco": forms.NumberInput(
                attrs={
                    "class": "input",
                    "min": "0",
                    "placeholder": "Preço do Produto",
                    "step": "0.01",
                }
            ),

        }