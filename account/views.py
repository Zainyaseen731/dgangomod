from django.shortcuts import render
from django.http import HttpResponse
from .form import SearchForm
from django.contrib.auth.models import User

def register(request):
    form=SearchForm(request.POST or None)
    if form.is_valid():
        first_name=(form.cleaned_data.get("first_name"))
        last_name=(form.cleaned_data.get("last_name"))
        username=(form.cleaned_data.get("username"))
        email=(form.cleaned_data.get("email"))
        password1=(form.cleaned_data.get("password1"))
        password2=(form.cleaned_data.get("password2"))
        print(first_name)
        print(last_name)
        print(username)
        print(email)
        print(password1)
        print(password2)
        
    return render(request,"form.html",{'form':form})