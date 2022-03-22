from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import inventories, TruckExpense
from django import forms


class create_form(ModelForm):
    class Meta:
        model = inventories
        fields = "__all__"

        widgets = {
        'created_at': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(create_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white',
        })



class TruckExpForm(ModelForm):
    class Meta:
        model = TruckExpense
        fields = "__all__"

        widgets = {
        'created_at': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(TruckExpForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white',
        })
