from django.forms import ModelForm
from drugshop.models import product, stock


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
