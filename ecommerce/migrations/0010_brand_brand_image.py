# Generated by Django 4.1 on 2023-02-15 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_alter_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_image',
            field=models.ImageField(default='image', upload_to='static/ecommerce/images'),
            preserve_default=False,
        ),
    ]
