# Generated by Django 4.1 on 2023-02-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_alter_order_product_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.CharField(max_length=200, null=True),
        ),
    ]