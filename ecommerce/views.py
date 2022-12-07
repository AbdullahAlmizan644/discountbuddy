from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"ecommerce/index.html")

def product_details(request):
    return render(request,"ecommerce/product_details.html")


def cart(request):
    return render(request,"ecommerce/cart.html")


def checkout(request):
    return render(request,"ecommerce/checkout.html")


def thankyou(request):
    return render(request,"ecommerce/thankyou.html")

def about(request):
    return render(request,"ecommerce/about.html")


def contact(request):
    return render(request,"ecommerce/contact.html")


def category(request):
    return render(request,"ecommerce/category.html")


