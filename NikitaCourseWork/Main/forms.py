from django import forms

CHOICES = [('encrypt', 'encrypt'),
         ('decrypt', 'decrypt')]
class FormForFile(forms.Form):
    Mess = forms.CharField(max_length=1000, required=True)
    Key = forms.CharField(max_length=1000, required=True)
    Mess.widget.attrs.update({'placeholder': "Enter a message: ", 'name': "mes"})
    Key.widget.attrs.update({'placeholder': "Enter a key: ", 'name': "key"})
