from django.contrib import admin
from .models import Category,Product,Brand,Contact


admin.site.site_title="Discount Buddy Admin Dashboard"
admin.site.site_header="Discount Buddy Admin Dashboard"
admin.site.index_title="Welcome to Admin-dashboard"

# Register your models here.
admin.site.register((Category,Product,Brand,Contact))
