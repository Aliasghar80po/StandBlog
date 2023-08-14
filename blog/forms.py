from django import forms
from django.core.exceptions import ValidationError
from .models import Message


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=10, label='your name :')
    text = forms.CharField(max_length=100, label='your massage :')
    ege = forms.IntegerField(max_value=10)
    email = forms.EmailField()
    birth_year = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('NAME AND TEXT ARE SAME', code='name_text_same')

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if '@' or '#' or '!' or '&' or '*' or '^' or '%' or '$' in name:
    #         raise ValidationError('this "@" or "#" or "!" or "&" or "* or "^" or "%" or "%" con not be in name')
    #     return name


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "ENTER YOUR TITLE"
            }),
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "ENTER YOUR TEXT"
            })
        }


class SearchForm(forms.Form):
    search_input = forms.CharField(label='Search', max_length=100)
    result_input = forms.CharField(label='Result', max_length=100)
