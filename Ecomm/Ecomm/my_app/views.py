from django.http import HttpResponse
from django.shortcuts import redirect, render
from my_app.form import ProductForm
from my_app.models import Cart, Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.core.mail import send_mail
from django.conf import settings
from .models import Product, Review




# Create your views here.
def home(request):
    return render(request,'index.html')
def pro(request):
    L=Product.objects.all()
    return render(request,'products.html',{'prdt': L})
def new(request):
   return HttpResponse ("success")
def add(request):
    if request.method=="POST":
        pf=ProductForm(request.POST,request.FILES)
        if pf.is_valid():
            pf.save()
            return redirect('pro')
        else:
            return HttpResponse("Invalid form")
    f=ProductForm()
    return render(request,'add_products.html',{'form':f})

def delete_product(request,pro_id):
    p=Product.objects.get(id=pro_id)
    p.delete()
    return redirect('pro')
def edit(request,pro_id):
    p=Product.objects.get(id=pro_id)
    f=ProductForm(request.POST or None,request.FILES or None ,instance=p)
    if f.is_valid():
        f.save()
        return redirect('pro')
    return render(request,'add_products.html',{'form': f})

def search(request):
    n=request.POST['pname']
    p=Product.objects.filter(name=n)
    return render(request,'products.html',{'prdt': p})

def signup(request):
    if request.method=='POST':
        uname=request.POST['uname'] 
        password=request.POST['pswd']
        first=request.POST['fname']
        last=request.POST['lname']
        em=request.POST['email']
        myuser=User.objects.create_user(username=uname,password=password,email=em)
        myuser.first_name=first
        myuser.last_name=last
        myuser.save()
        return redirect('signin')
    return render(request, "signup.html")
def signin(request):
    if request.method == 'POST':
        urname = request.POST['uname']
        pword = request.POST['pswd']
        red = authenticate(username=urname, password=pword)
        print(red)
        if red is not None:
            login(request, red)
            f = red.first_name
            l = red.last_name
            return render(request, "user_dashboard.html", {'fname': f,'lname':l})
        else:
            return render(request, "signin.html", {'error': 'Invalid username or password. Please try again.'})

    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return render(request,'index.html')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)

    for item in cart_items:
        item.subtotal = item.product.price * item.quantity

    total = sum(item.subtotal for item in cart_items)

    return render(request, 'Cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('view_cart')




def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product).order_by('-created_at')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        # Save the review
        Review.objects.create(product=product, name=name, email=email, comment=comment)

        # Send email
        send_mail(
            subject=f'New Review for {product.name}',
            message=f'Name: {name}\nEmail: {email}\nComment: {comment}',
            from_email='najiya18@gmail.com',
            recipient_list=['najiya18@gmail.com'],
            fail_silently=False,
        )

        return redirect('product_detail', product_id=product.id)

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews
    })
