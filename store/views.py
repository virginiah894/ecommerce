from unicodedata import category
from django.shortcuts import render, redirect
from.models import Product, Order,Category

# Create your views here.
def home(request):
    products= Product.objects.all()
    orders = Order.objects.all()
    category = Category.objects.all

    return render(request,'index.html',locals())
