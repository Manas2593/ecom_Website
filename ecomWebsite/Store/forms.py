from django import forms
from Store.models import *

# Create your forms here

class ProductCreationForm(forms.Form):
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ('owner',)