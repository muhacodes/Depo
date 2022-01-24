from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Salary


class create_form(ModelForm):
    class Meta:
        model = Salary
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(create_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white',
        })
