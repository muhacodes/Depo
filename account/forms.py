from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import ChoiceWidget, PasswordInput
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from django import forms
from .backend import Backend


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
    

class LoginForm(forms.Form):
    # password = forms.CharField(widget=forms, PasswordInput, required=True)
    username = forms.CharField(max_length=255, required=True)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = Backend.authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = Backend.authenticate(email=email, password=password)
        return user

    

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        # other customization 