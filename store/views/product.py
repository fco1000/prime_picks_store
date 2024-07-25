from django.shortcuts import render
from store.models.products import Product

def productView(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'shop-single.html',context)