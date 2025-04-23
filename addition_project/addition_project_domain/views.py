from django.shortcuts import redirect, render
from .forms import category_create_form, product_create_form,customer_create_form,order_create_form,order_product_create_form
from .models import Category,Product

def index(request, category_id=None):
    categories = Category.objects.all().order_by('sequence').values()
    if category_id is None:
        products = Product.objects.all().order_by('sequence').values()
        return render(request, 'home/index.html', {'categories': categories,'products': products})
    products = Product.objects.filter(category_id=category_id).order_by('sequence').values()
    return render(request, 'home/index.html', {'categories': categories,'products': products})

def create_category(request):
    if request.method == "POST":
        form = category_create_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = category_create_form()
    return render(request, 'categories/create-category.html', {'form': form})

def create_product(request):
    if request.method == "POST":
        form = product_create_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = product_create_form()
    return render(request, 'products/create-product.html', {'form': form})

def create_customer(request):
    if request.method == "POST":
        form = customer_create_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = customer_create_form()
    return render(request, 'customers/create-customer.html', {'form': form})

def create_order(request):
    if request.method == "POST":
        form = order_create_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = order_create_form()
    return render(request, 'orders/create-order.html', {'form': form})

def create_order_product(request):
    if request.method == "POST":
        form = order_product_create_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = order_product_create_form()
    return render(request, 'orders/create-order-product.html', {'form': form})