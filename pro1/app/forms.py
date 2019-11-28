from django import forms
from .models import MerchantMdel
from .models import ProductModel

class Merchentnewpassword(forms.ModelForm):
    class Meta:
        model=MerchantMdel
        fields="__all__"

class MerchantProduct(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields="__all__"