from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class loginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'input100'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'input100'}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password and repeat_password and password != repeat_password:
            raise ValidationError("Passwords do not match.")
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    widgets = {
        "user_permissions": forms.SelectMultiple(attrs={
            "class": "form-control"
        }),
        "image": forms.FileInput(attrs={
            "class": "form-control-file"
        })
    }

# dropdown-menu