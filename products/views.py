from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from checkout.models import Order
from .forms import ProductForm, CategoryForm


""" Products """


def get_products(request):
    """ A view to return the shop page """
    products = Product.objects.all()
    categories = Category.objects.all()
    current_category = None

    if 'category' in request.GET:
        current_category = request.GET['category'].split(',')
        products = products.filter(category__name__in=current_category)
        current_category = current_category[0].capitalize()

    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category
    }

    return render(request, 'products/products.html', context)


def view_product(request, product_id):
    """ A view to show the product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)


@login_required
def product_management(request):
    """ A view to show the product management page """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product_count = Product.objects.count()
    order_count = Order.objects.count()

    context = {
        'product_count': product_count,
        'order_count': order_count
    }

    return render(request, 'products/manage.html', context)


@login_required
def create_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(reverse('view_product', args=[product.id]))
        else:
            print("fail save")
    else:
        form = ProductForm()

    template = 'products/create_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def create_category(request):
    """ Add a category to the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    categories = Category.objects.all()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect(reverse('product_management'))

    else:
        form = CategoryForm()

    template = 'products/create_category.html'
    context = {
        'form': form,
        'categories': categories
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_product', args=[product.id]))
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('products'))
