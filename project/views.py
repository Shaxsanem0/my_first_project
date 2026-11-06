from django.shortcuts import render
from .models import Product

def home_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)