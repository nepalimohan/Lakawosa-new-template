# Generated by Django 4.0.6 on 2022-07-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('Jeans', 'Jeans'), ('Tshirt', 'Tshirt'), ('Shoes', 'Shoes'), ('Hoodie', 'Hoodie'), ('Jacket', 'Jacket'), ('Bag', 'Bag')], max_length=100),
        ),
    ]
