from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):   

    allprods = []

    categoriesProducts = Product.objects.values('category')
    categories = {
        item['category'] for item in categoriesProducts
    }
    for cat in categories:
        product = Product.objects.filter(category = cat)
        n = len(product)
        nSlides = ((n//4) + ceil((n/4) - (n//4)))
        allprods.append([product,range(1,nSlides),nSlides])

    params = {
        'allprods':allprods
    }
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')