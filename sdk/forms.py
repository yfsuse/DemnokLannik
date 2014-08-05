from django import forms


class YeahTestForm(forms.Form):
    keywords = forms.CharField()
    filepath = forms.FileField()
