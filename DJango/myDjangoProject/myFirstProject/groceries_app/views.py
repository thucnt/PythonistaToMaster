from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from .models import RegisteredUser
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def app_homepage(request):
    try:
        if usrnme:
            userDetails = {'username': usrnme}
            return render(request, "loggedin.html", userDetails)
    except NameError:
        return render(request, 'homepage.html')

def about_us(request):
    try:
        if usrnme:
            return render(request, "aboutUs.html")
    except NameError:
        return render(request, 'homepage.html')

def services(request):
    try:
        if usrnme:
            return render(request, "services.html")
    except NameError:
        return render(request, 'homepage.html')


def contact_us(request):
    try:
        if usrnme:
            return render(request, "contactUs.html")
    except NameError:
        return render(request, 'homepage.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("signin")
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, "register.html", user_info)

def signin(request):
    global usrnme
    if request.method == 'POST':
        usrnme = request.POST['username']
        psswrd = request.POST['pswd']

        try:
            user = RegisteredUser.objects.get(name=usrnme)
            if usrnme == user.name and psswrd == user.password:
                return redirect("loggedin")
            else:
                messages.info(request, "Incorrect password.")
                return redirect("signin")
        except ObjectDoesNotExist:
            messages.info(request, "The user do not exist.")
            return redirect("signin")
    else:
        return render(request, "signin.html")

def loggedin(request):
    userDetails = {'username': usrnme}
    return render(request, "loggedin.html", userDetails)

def logout(request):
    global usrnme
    del usrnme
    return render(request, "logout.html")