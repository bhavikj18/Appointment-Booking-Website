from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import person
from django.core.mail import send_mail


# Create your views here.
def index(request):
    usernametop = request.user.username
    if request.user.is_anonymous:
        return redirect("/login")
    return render (request ,'index.html', {'usernametop':usernametop})

def regis(request):
    usernametop = request.user.username
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used!')
                return redirect('/login')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('/login')
        else:
            messages.info(request, 'rentered password does not match!')
            return redirect('/login')
    else:
        return render(request , 'register.html', {'usernametop':usernametop})


def loginUser(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user, password=password) 
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render (request ,'login.html')
    return render(request ,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def aboutus(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render (request ,'about.html')

def docss(request):
    loperson = person.objects.all()
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == 'POST':
        doc_mail = request.POST.get('docmail')
        patientpho = request.POST.get('phono')
        patientmail = request.POST.get('mail')
        patientreason = request.POST.get('reason')
        message_name = request.user.username
        message_email = 'medaidappointments@gmail.com'
        message = f"{message_name} wants to book an appointment with you.\n\nPATIENT DETAILS:-\nPHONE: {patientpho}\nEMAIL: {patientmail}\n\n{patientreason}\nThank you."
        send_mail(
            message_name,
            message,
            message_email,
            [doc_mail,],
            fail_silently = False,
        )
    return render (request ,'docss.html', {'loperson':loperson})

def prescrip(request):
    usernametop = request.user.username
    if request.user.is_anonymous:
        return redirect("/login")
    return render (request ,'prescription.html', {'usernametop':usernametop})

def appoint(request):
    usernametop = request.user.username
    loperson = person.objects.all()
    if request.user.is_anonymous:
        return redirect("/login")
    return render (request ,'appointments.html', {'loperson':loperson})

def certif(request):
    usernametop = request.user.username
    if request.user.is_anonymous:
        return redirect("/login")
    return render (request ,'certificates.html', {'usernametop':usernametop})

def team(request):
    usernametop = request.user.username
    if request.user.is_anonymous:
        return redirect("/login")
    return render (request ,'teams.html', {'usernametop':usernametop})