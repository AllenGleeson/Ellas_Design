from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.

def get_products(request):
    """ A view to return the shop page """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def view_product(request, product_id):
    """ A view to show the product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)