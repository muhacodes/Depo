from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Expense, ExpenseType


class create_form(ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(create_form, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white',
        })



class expense_type(ModelForm):
    class Meta:
        model = ExpenseType
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(expense_type, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: white',
        })
