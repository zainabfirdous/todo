from dataclasses import fields
from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
       #Title = forms.CharField(max_length=200)
       #Description = forms.CharField(max_length=400)
       #Date = forms.DateField(widget=forms.SelectDateWidget)
       model = Todo
       fields = "__all__"