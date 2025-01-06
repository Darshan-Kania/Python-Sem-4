from django.http import HttpResponse
from django.shortcuts import render
from django import forms
# Create your views here.


def home(request):
    return render(request, 'Calc.html')


def add(request):
    if request.method == 'POST':
        data = int(request.POST.get('num1'))
        data2 = int(request.POST.get('num2'))
        ans = data+data2
    return HttpResponse(ans)
