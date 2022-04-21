from dataclasses import field, fields
from datetime import datetime
from django import forms

from books.models import Author, Book

Appropriate_CHOICES =(
    ("child","under 8"),
    ("between","8-15"),
    ("adult","adults")
)

class CreateBookForm(forms.Form):
    name=forms.CharField(label="name")
    publish_date=forms.DateField(label="publish_data")
    add_to_site=forms.DateField( label="add_to_site")
    author = forms.ModelChoiceField(queryset=Author.objects.only('name'))
    price=forms.FloatField(label="price")
    appropriate=forms.ChoiceField(choices= Appropriate_CHOICES , label="appropriate")
    # image=forms.FileField(label="image")


class CreateAuthorForm (forms.Form):
        name=forms.CharField( label="name")

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
