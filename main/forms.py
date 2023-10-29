from django.forms import ModelForm, TextInput, Textarea
from .models import task

class taskForm(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название'
                }),
            'task': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание задачи'   
                })
        }