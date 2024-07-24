
from store.models.products import Product
from store.models.category import Category
from django.shortcuts import render

def shop(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop.html', data)