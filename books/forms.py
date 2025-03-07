from .models import Books
from django.forms import forms, Form, ModelForm

class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

