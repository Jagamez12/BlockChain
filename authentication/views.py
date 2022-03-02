import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def singup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']  
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.First_name = fname
        myuser.Last_name = lname
    
        myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('singin')


    return render(request,"authentication/singup.html")

def singin(request):

    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username = username, pass1 = pass1)

        if user is not None:
            login(request, user)
            fname = user.First_name
            print(fname)
            return redirect(request,'authentication/index.html', {'fname': fname})
        else:
            messages.error(request, "bad credentials")
            return redirect('home')

    return render(request,"authentication/singin.html")

def singout(request):
    pass

