from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Rate
from django import forms


class create_form(ModelForm):
    class Meta:
        model = Rate
        exclude = ('dollars',)

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
