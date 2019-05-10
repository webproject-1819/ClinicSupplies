from django.forms import ModelForm

from drugshop.models import product, stock, sale

class productForm(ModelForm):
    class Meta:
        model = product
        fields = "__all__"
        exclude = ('user',)

class stockForm(ModelForm):
    class Meta:
        model = stock
        fields = "__all__"
        exclude = ('user',)

class salesForm(ModelForm):
    class Meta:
        model = sale

        fields = ('discount',)
