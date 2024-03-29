from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact,Product,Category,Brand,Order
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
import re
import json
from tabulate import tabulate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(request):
    categories=Category.objects.all()
    products=Product.objects.all()[3:8]
    return render(request,"ecommerce/index.html",{
        'categories':categories,
        'products':products,
    })



def cart(request):
    return render(request,"ecommerce/cart.html")



def checkout(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            first_name=request.POST.get("fname")
            last_name=request.POST.get("lname")
            address=request.POST.get("address")
            state=request.POST.get("state")
            zip=request.POST.get("zip")
            email=request.POST.get("email")
            phone=request.POST.get("phone")
            notes=request.POST.get("notes")
            total_price=request.POST.get("total")
            all_product=request.POST.get("all")

            print(all_product,total_price)

            data=json.loads(all_product)

            product_list=[]

            count=1
            for d in data:
                product_list.append([f"product{count} name:{d['name']}, product{count} quantity: {d['quantity']}, product{count} price:{d['price']}"])
                count=count+1
            
           
            product_list=tabulate(product_list,tablefmt="grid")
            print(product_list)



            order=Order(first_name=first_name,last_name=last_name,address=address,state=state,
            zip=zip,email=email,phone=phone,notes=notes,total_price=total_price,product_list=product_list,username=request.user)
            order.save()
            messages.success(request,"Thanks for your orders")
            return redirect(thankyou)
        return render(request,"ecommerce/checkout.html")
    else:
        return redirect(user_login)


def order_history(request):
    if request.user.is_authenticated:
        order_list=Order.objects.filter(username=request.user).all()
        print(order_list)
        return render(request,"ecommerce/order_history.html",{
            "order_list":order_list
        })
    else:
        return redirect(user_login)


def thankyou(request):
    if request.user.is_authenticated:
        return render(request,"ecommerce/thankyou.html")
    else:
        return redirect(user_login)


def about(request):
    return render(request,"ecommerce/about.html")


def contact(request):
    if request.method=="POST":
        first_name=request.POST["fname"]
        last_name=request.POST["lname"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        
        if len(first_name)<3 or len(last_name)<3 or len(subject)<3 or len(email)<3 or len(message)<3:
            messages.error(request,"Please fill the form correctly.")

        else:
            contact=Contact(first_name=first_name,last_name=last_name,email=email,subject=subject,message=message)
            contact.save()
            messages.success(request,"Thanks for your message")
            return redirect("contact")
    return render(request,"ecommerce/contact.html")




def shop(request, **kwargs):
    products=Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    categories=Category.objects.all()
    print(categories[1])
    return render(request,"ecommerce/shop.html",{
        "products":products,
        "categories":categories,

    })


def product_details(request,id,slug):
    product=Product.objects.filter(id=id,title=slug).first()
    print(product.category)
    related_product=Product.objects.filter(category=product.category).all()
    print(related_product)
    return render(request,"ecommerce/product_details.html",{
        "product":product,
        "related_product":related_product,
    })




def category(request,id):
    products=Product.objects.filter(category=id)
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


    categories=Category.objects.all()
    category=Category.objects.filter(id=id).first()
    brands=Brand.objects.filter(category=id)
    return render(request,"ecommerce/category.html",{
        'products':products,
        'category':category,
        'categories':categories,
        'brands':brands,
    })


def brand(request,id):
    brand_details=Brand.objects.filter(id=id).first()
    products=Product.objects.filter(brand=id)
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 9)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    categories=Category.objects.all()

    return render(request,"ecommerce/brand.html",{
        "products":products,
        'categories':categories,
        'brand_details':brand_details,
    })


def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            messages.success(request,"Logged in successfully.")
            return redirect("/")

        else:
            messages.error(request,"wrong username or password")
            return redirect("login")

    return render(request, "ecommerce/login.html")



def user_logout(request):
    logout(request)
    messages.success(request,"Logged out successfully.")
    return redirect("/")


def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        user=User.objects.filter(username=username).first()

        if user:
            messages.error(request,"Username already exist")

        elif len(username)<4:
            messages.error(request,"User must be greater than 4 words ")

        elif len(email)<4:
            messages.error(request,"email must be greater than 4 words ")

        elif len(password)<4:
            messages.error(request,"password must be greater than 8 digits")

        elif password!=confirm_password:
            messages.error(request,"password doesn't match")

        else:
            new_user=User.objects.create_user(username=username,email=email,password=password)
            new_user.save()
            messages.success(request,"your registration complete successfully.")
            return redirect("login")

    return render(request, "ecommerce/signup.html")





def search_result(request):
    if request.method=="POST":
        search=request.POST.get("search")
        print(search)

        if search!="":
            products = Product.objects.filter(title__icontains=search).all()

            if products:
                print(products)
                return render(request, "ecommerce/search_result.html",{
                    "products":products,
                    "search":search,
                })
            else:
                messages.success(request,f"no match with result:{search}")
                return redirect("/")

        
        else:
            messages.success(request,"Please enter a product name")
            return redirect("/")