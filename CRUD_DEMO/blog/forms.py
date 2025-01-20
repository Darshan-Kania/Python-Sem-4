from django import forms
from .models import BlogModel
class BlogForms(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = [
            'title', 'description'
            ]