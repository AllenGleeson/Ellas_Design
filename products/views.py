from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import Http404
import sys
import os
# Add project root to path to import product_data
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ella-moya'))
from product_data import get_all_products, get_product_by_id, get_all_categories


@xframe_options_exempt
def get_products(request):
    """A view to return the shop page - read only"""
    products = get_all_products()
    categories = get_all_categories()
    current_category = None

    # Filter by category if specified
    if 'category' in request.GET:
        category_names = request.GET['category'].split(',')
        products = [p for p in products if p.category and p.category.name in category_names]
        if products and products[0].category:
            current_category = products[0].category.name

    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category
    }

    return render(request, 'products/products.html', context)


@xframe_options_exempt
def view_product(request, product_id):
    """A view to show the product - read only, no reviews or forms"""
    product = get_product_by_id(product_id)
    
    if not product:
        raise Http404("Product not found")

    # Disable reviews for showcase
    reviews = []  # Empty list - no reviews
    
    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/view_product.html', context)
