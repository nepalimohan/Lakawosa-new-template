from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def products(request):
    products = Product.objects.all()
    data = {
        'products': products,
    }
    return render(request, 'pages/products.html', data)

def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    data = {
        'product':product,
    }
    return render(request,'pages/product-details.html', data)