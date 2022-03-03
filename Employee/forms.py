from django.forms import ModelForm, widgets
from .models import Employee
from django import forms

class create_form(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'joined': widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(create_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white',
        })
