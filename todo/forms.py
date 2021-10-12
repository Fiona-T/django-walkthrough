from django import forms
from .models import Item


# class inheriting from django class to create form
class ItemForm(forms.ModelForm):
    # inner class whcih gives form info about itself
    class Meta:
        # model is our Item model
        model = Item
        # fields are the two fields from the model
        fields = ['name', 'done']
