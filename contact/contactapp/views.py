from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .models import registration, contacts


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        if registration.objects.filter(email = email, password=password).exists():
            print("success")
            return redirect('/home')

        else:
            messages.info(request, 'Invalid Credentials')
            print("error")
            return redirect('/')
    else:
        return render(request, 'signin.html')

def signuppage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        secpass = request.POST['spass']
        data = registration(email=email, password=password, secretpassword=secpass)
        data.save()
        return redirect('/')
        print("Saved")
    else:
        return  render(request, 'signup.html')

def homepage(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        data = contacts(name=name, phone=phone, email=email)
        data.save()
        return redirect('/home')
    else:
        allcontacts = contacts.objects.all()
        return render(request,'homepage.html',{'contact':allcontacts})
