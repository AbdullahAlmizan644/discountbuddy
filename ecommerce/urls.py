from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("product_details/<int:id>/<str:slug>",views.product_details,name="product_details"),
    path("category/<int:id>",views.category,name="category"),
    path("brand/<int:id>",views.brand,name="brand"),
    path("shop",views.shop,name="shop"),
    path("cart",views.cart,name="cart"),
    path("checkout",views.checkout,name="checkout"),
    path("contact",views.contact,name="contact"),
    path("thankyou",views.thankyou,name="thankyou"),
    path("about",views.about,name="about"),
    path("login",views.user_login,name="login"),
    path("signup",views.signup,name="signup"),
    path("user_logout",views.user_logout,name="user_logout"),

]

