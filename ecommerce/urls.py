from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("product_details",views.product_details,name="product_details"),
    path("Category",views.category,name="category"),
    path("cart",views.cart,name="cart"),
    path("checkout",views.checkout,name="checkout"),
    path("contact",views.contact,name="contact"),
    path("thankyou",views.thankyou,name="thankyou"),
    path("about",views.about,name="about"),
]