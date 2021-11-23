from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    diction={
    "test":"Hello World"
    }
    return render (request,"myapp/index.html",context=diction)


def form(request):
    new_form=forms.user_forms()
    diction={
    "test_form":new_form,
    "heading":"This from is created by django library"
    }
    return render(request,"myapp/form.html",context=diction)
