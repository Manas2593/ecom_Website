from django.forms import ModelForm
from Store.models import *

# Create your forms here

class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'