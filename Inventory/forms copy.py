from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Stock


class AddStock(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AddStock, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })