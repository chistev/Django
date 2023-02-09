from . import models
from django import forms
from django.forms import ModelForm


class TaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = '__all__'
