from django.shortcuts import render, redirect, get_object_or_404
from core.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from .models import userdata
from .forms import ContactForm
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        image=request.FILES.get('image')
        details=Customers.objects.create(name=name, address=address, phone=phone, email=email, picture=image)
        details.save()
        print(name,address,phone,email)
        return redirect("home")
    return render(request, 'customer.html')

def viewcustomer(request):
    customersdetail = Customers.objects.all()
    context={
        'customers':customersdetail,
    }
    print(customersdetail)
    return render(request, 'view.html', context)

def editcustomer(request,id):
    data2 = get_object_or_404(Customers, id=id)
    context={
        'data2':data2
    }
    print(f"the name is {data2.name}")
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        image=request.FILES.get('image')
        data2.name=name
        data2.address=address
        data2.phone=phone
        data2.email=email
        if image: 
            data2.picture = image
        data2.save()
        return redirect('view')
    return render(request, 'customer.html')

def deletecustomer(request,id):
    datadelete = Customers.objects.filter(id=id)
    print(datadelete)
    datadelete.delete()
    return redirect('view')
    return render(request, 'view.html')

def registerproduct(request):
    if request.method=='POST':
        name=request.POST.get('product_name')
        price=request.POST.get('price')
        pic=request.FILES.get('productimage')
        print(pic)
        data=Products.objects.create(name=name,price=price,picture=pic)
        data.save()
        return redirect("viewproduct")
    return render(request, 'product.html')

def viewproduct(request):
    productdetails=Products.objects.all()
    context={'productdetails':productdetails}
    return render(request, 'products.html',context)


def editproduct(request, id):
    product = get_object_or_404(Products, id=id)
    
    if request.method == 'POST':
        name = request.POST.get('product_name')
        price = request.POST.get('price')
        pic = request.FILES.get('productimage')
        product.name = name
        product.price = price
        if pic: 
            product.picture = pic
        product.save()
        return redirect('viewproduct')
    return render(request, 'product.html', {'product': product})

def deleteproduct(request,id):
    data = Products.objects.filter(id=id)
    data.delete()
    return redirect("viewproduct")
    return render(request, 'products.html')



def regorlog(request):
    if request.method == 'POST':
        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'signup':
                username = request.POST.get('rusername')
                password = request.POST.get('rpassword')
                encrypted_password = make_password(password)
                data = userdata.objects.create(Username=username, Password=encrypted_password)
                data.save()
                print(f"Signup - Username: {username}, Password: {password}")

            elif action == 'login':
                username = request.POST.get('username')
                password = request.POST.get('pswd')
                
                user_data = userdata.objects.filter(Username=username).first()
                if user_data:
                    if check_password(password, user_data.Password):
                        return redirect('home')
                    else:
                        print('Incorrect password')
                else:
                    print('Username not found')
                    
    return render(request, "registration and login.html")


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                subject=f"Contact Us message from {name}",
                message=f'This message is from {email}\n{message}',
                from_email=email,
                recipient_list=['adhikarianmol5@gmail.com'],
            )
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

