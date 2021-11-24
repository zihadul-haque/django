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

    if request.method=='POST':
        new_form=forms.user_forms(request.POST)

        if new_form.is_valid():
            user_name=new_form.cleaned_data['user_name']
            user_dob=new_form.cleaned_data['user_dob']
            user_email=new_form.cleaned_data['user_dob']

            diction.update({"user_name":user_name})
            diction.update({"user_dob":user_dob})
            diction.update({"user_email":user_email})

            diction.update({'form_submitted':"Yes"})

    return render(request,"myapp/form.html",context=diction)
