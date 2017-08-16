from django.contrib.auth.models import User
from django import forms
from .models import Shop, Product, Commercant


class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ['shop_name', 'shop_logo']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['product_name', 'product_price', 'product_logo','product_pic1', 'product_pic2','product_pic3', 'product_type', 'category', 'description', 'quantite', 'is_activate']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CommercantForm(forms.ModelForm):

    class Meta:
        model = Commercant
        fields = ['name', 'description', 'picture', 'tel', ]

