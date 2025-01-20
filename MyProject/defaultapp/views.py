from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import MyForm
from .models import MyModel
# Create your views here.


def add(request):
    if request.method == 'POST':
        data = int(request.POST.get('num1'))
        data2 = int(request.POST.get('num2'))
        ans = data+data2
        return render(request, 'Calc.html', {'ans': ans})


def home(request):
    return render(request, 'Home.html')


def myView(request):
    if request.method=='POST':
        form=MyForm(request.POST)
        if form.is_valid():
            form.save();
            return redirect("Sucess")
    else:
        form=MyForm()
    return render(request, 'formpractice.html', {'form': form})