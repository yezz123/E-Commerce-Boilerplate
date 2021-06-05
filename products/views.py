from django.shortcuts import render
from .models import Product

# Create your views here.
def products_fill(request):
    products = Product.objects.all()
    return render(request, "", {"products": products})
    # between "" you can post your html page "product.html"