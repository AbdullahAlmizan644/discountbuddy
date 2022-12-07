from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Brand(models.Model):
    category=models.ForeignKey(Category,models.CASCADE)
    brand=models.CharField(max_length=200)

    def __str__(self):
        return self.brand

class Product(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category,models.CASCADE)
    brand=models.ForeignKey(Brand,models.CASCADE)
    tagline=models.CharField(max_length=100)
    description=models.CharField(max_length=10000)
    image=models.ImageField(upload_to='static/ecommerce/images')
    price=models.IntegerField()
    discount=models.IntegerField()
    discount_price=models.IntegerField()
    date=models.DateField()


    def __str__(self):
        return f"product:{self.title}    Category:{self.category}"