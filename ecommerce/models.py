from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='static/ecommerce/images')

    def __str__(self):
        return self.category


class Brand(models.Model):
    category=models.ForeignKey(Category,db_column='category',on_delete=models.CASCADE)
    brand=models.CharField(max_length=200)

    def __str__(self):
        return self.brand

class Product(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category,models.CASCADE)
    brand=models.ForeignKey(Brand,models.CASCADE)
    tagline=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='static/ecommerce/images')
    price=models.IntegerField()
    discount=models.IntegerField()
    discount_price=models.IntegerField()
    date=models.DateField()


    def __str__(self):
        return f"Product :{self.title} Category :{self.category}  Brand:{self.brand} "


class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return f"message from {self.last_name}"