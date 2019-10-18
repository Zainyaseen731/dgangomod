from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .form import SearchForm,DataStore
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def main(request): 
    context={
    }
    template="main.html"
    return render(request,template,context)


@login_required
def home(request):
    qs=Post.objects.all()
    context={
        'object':qs
    }
    template="detail.html"
    return render(request,template,context)


def signup(request):
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

        if password1==password2:
            if User.objects.filter(username=username).exists():
                #raise forms.ValidationError("You cannot post more than once every x minutes")
                messages.info(request,"User name taken")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is taken")
                return redirect('/signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                email=email,password=password1)
                user.save()
                return redirect('/login')
        
    return render(request,"form.html",{'form':form})


def login(request):
    form1=DataStore(request.POST or None)
    if form1.is_valid():
        username=(form1.cleaned_data.get("username"))
        password=(form1.cleaned_data.get("password"))
        print(username)
        print(password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            return redirect('/login')
    return render(request,"in.html",{'form':form1})
