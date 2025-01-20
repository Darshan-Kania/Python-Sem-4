import django.forms as forms
from .models import MyModel
class MyForm(forms.ModelForm):
    name=forms.CharField(label="Name",max_length=100)
    email=forms.EmailField(label="Email")
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    class Meta:
        model = MyModel
        fields = ['name', 'email']