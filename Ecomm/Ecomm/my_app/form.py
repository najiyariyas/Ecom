from django  import forms
from my_app.models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the name of the product','style': 'width: 300px;','size': '40'}),
            'desc':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the description  of the product','style': 'width: 300px;'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the price of product','style': 'width: 300px;'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the stock of product','style': 'width: 300px;'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'upload image  of product','style': 'width: 300px;'}),
            'cat':forms.Select(attrs={'class':'form-control','placeholder':'Enter the category of product','style': 'width: 300px;'})
               }
   