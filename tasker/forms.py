from django import forms
from markdownx.fields import MarkdownxFormField
from .models import Task, Summary


class TaskForm(forms.ModelForm):
    """Taskのフォーム"""
    class Meta:
        model = Task
        fields = ('name', 'category', 'pri', 'time', 'rgst', 'status')
        labels = {
            'name': 'name',
            'category': 'category',
            'pri': 'priority',
            'time': 'time taken',
            'rgst': 'registration date',
            'status': 'done',
        }


class SummaryForm(forms.ModelForm):
    """Summaryのフォーム"""
    class Meta:
        model = Summary
        fields = ('title', 'summary', )
        labels = {
            'title': 'title',
            'summary': 'summary',
        }
        summary = MarkdownxFormField()
        widgets = {
            'title': forms.TextInput(attrs={'size': "50"}),
            'summary': forms.Textarea(attrs={'rows': 6, 'cols': 22, 'style': 'resize:none;'})
        }
