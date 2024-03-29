from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Review
from checkout.models import Order
from .forms import ProductForm, CategoryForm, ReviewForm
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def get_products(request):
    """ A view to return the shop page """
    products = Product.objects.all()
    categories = Category.objects.all()
    current_category = None

    if 'category' in request.GET:
        current_category = request.GET['category'].split(',')
        products = products.filter(category__name__in=current_category)
        current_category = current_category[0]

    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category
    }

    return render(request, 'products/products.html', context)

@xframe_options_exempt
def view_product(request, product_id):
    """ A view to show the product and any reviews """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all().filter(product=product)
    paginator = Paginator(reviews, 7) # Show 7 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        user_review = ReviewForm(request.POST)
        if user_review.is_valid():
            user_review.instance.product = product
            user_review.save()
            user_review = ReviewForm()
            return redirect(reverse('view_product', args=[product.id]))
    else:
        user_review = ReviewForm()

    context = {
        'product': product,
        'reviews': page_obj,
        'user_review': user_review
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
