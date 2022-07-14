from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

product_choices = (
    ('Men', 'Men'),
    ('Women', 'Women'),
)

category_choices = (
    ('Jeans', 'Jeans'),
    ('Tshirt', 'Tshirt'),
    ('Shoes', 'Shoes'),
    ('Hoodie', 'Hoodie'),
    ('Jacket', 'Jacket'),
    ('Bag', 'Bag'),
)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_type = models.CharField(choices=product_choices, max_length=10)
    product_category = models.CharField(choices=category_choices ,max_length=100)
    description = RichTextField()
    brand = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='photo/%Y/%m/%d/')
    
    def __str__(self):
        return self.product_name