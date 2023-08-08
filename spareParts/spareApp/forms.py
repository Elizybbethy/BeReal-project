#handling forms to be displayed to the users.
from django.forms import ModelForm
from .models import *
# from spareApp.models import *

class AddForm(ModelForm): #this is the only filed workers will edit
    class Meta:
        model = Product
        fields = [
            "received_quantity" 
        ]

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = [
            "quantity", "amount_received", "issued_to"
        ]