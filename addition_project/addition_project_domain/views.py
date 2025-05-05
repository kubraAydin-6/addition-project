from django.shortcuts import get_object_or_404, redirect, render
from .forms import LoginForm, category_create_form, product_create_form,customer_create_form,order_create_form,order_product_create_form,KitchenOrderForm
from .models import Category,Product,order,customer, KitchenOrder
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request, category_id=None):
    categories = Category.objects.all().order_by('sequence').values()
    customers = customer.objects.all().order_by('name').values()
    return render(request, 'customers/customer-list.html', {'categories': categories,'customers': customers})

@login_required
def create_category(request):
    if request.method == "POST":
        form = category_create_form(request.POST)
        if form.is_valid():
            form.save()
            return category_list(request)
    else:
        form = category_create_form()
    return render(request, 'categories/create-category.html', {'form': form})

@login_required
def create_product(request):
    if request.method == "POST":
        form = product_create_form(request.POST)
        if form.is_valid():
            form.save()
            return product_list(request)
    else:
        form = product_create_form()
    return render(request, 'products/create-product.html', {'form': form})

@login_required
def create_customer(request):
    if request.method == "POST":
        form = customer_create_form(request.POST)
        if form.is_valid():
            form.save()
            return customer_list(request)
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

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get("userName"), password=form.cleaned_data.get("password"))

            if user is not None:
                print("test")
                login(request, user)
                return redirect('/home')
            else:
                messages.error(request, 'Kullanıcı adı veya şifre hatalı')
    return render(request, 'home/login.html', {'form': form})

def logout_user(request):
    logout(request)
    form = LoginForm()
    return render(request, 'home/login.html', {'form': form})

def ui_map(request):
    return render(request, 'home/ui-maps.html')

def ui_table(request):
    return render(request, 'home/ui-tables.html')

def ui_typography(request):
    return render(request, 'home/ui-typography.html')

def ui_notification(request):
    return render(request, 'home/ui-notifications.html')

@login_required
def category_list(request):
    categories = Category.objects.all().order_by('sequence').values()
    return render(request, 'categories/category-list.html', {'categories': categories})

@login_required
def product_list(request):
    products = Product.objects.all().order_by('sequence').values()
    return render(request, 'products/product-list.html', {'products': products})

@login_required
def invoice_list(request):
    orders = order.objects.all().order_by('created_at').values()
    return render(request, 'orders/invoice-list.html', {'invoices': orders})

def customer_list(request):
    customers = customer.objects.all().order_by('name').values()
    return render(request, 'customers/customer-list.html', {'customers': customers})

@login_required
def update_category(request, category_id):
    category= get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        form = category_create_form(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return category_list(request)
    else:
        form = category_create_form(instance=category)
    return render(request, 'categories/create-category.html', {'form': form})

@login_required
def update_product(request, product_id):
    product= get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = product_create_form(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return product_list(request)
    else:
        form = product_create_form(instance=product)
    return render(request, 'products/create-product.html', {'form': form})

@login_required
def update_customer(request, customer_id):
    get_customer= get_object_or_404(customer, pk=customer_id)
    if request.method == "POST":
        form = customer_create_form(request.POST,instance=get_customer)
        if form.is_valid():
            form.save()
            return customer_list(request)
    else:
        form = customer_create_form(instance=get_customer)
    return render(request, 'customers/create-customer.html', {'form': form})

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return category_list(request)

@login_required
def delete_customer(request, customer_id):
    deleted_customer = get_object_or_404(customer, pk=customer_id)
    deleted_customer.delete()
    return customer_list(request)

@login_required
def delete_product(request, product_id):
    deleted_product = get_object_or_404(Product, pk=product_id)
    deleted_product.delete()
    return product_list(request)

def select_customer(request, customer_id):
    selected_customer = get_object_or_404(customer, pk=customer_id)
    selected_customer.is_customer = True
    form = customer_create_form(request.POST,instance=selected_customer)
    if form.is_valid():
        form.save()
    get_category = Category.objects.all().order_by('sequence').values()
    products = Product.objects.all().order_by('sequence').values()
    return render(request, 'home/product-index.html', {'categories': get_category,'products': products})

def index_by_category(request, customer_id, category_id):
    categories = Category.objects.all().order_by('sequence').values()
    if category_id is not None:
        products = Product.objects.filter(category_id= category_id).order_by('sequence').values()
        return render(request, 'home/product-index.html', {'products': products,'categories': categories})
    products = Product.objects.all().order_by('sequence').values()
    return render(request, 'home/product-index.html', {'products': products,'categories': categories})
    
def kitchen_order_list(request):
    orders = KitchenOrder.objects.filter(is_prepared=False)
    return render(request, 'kitchen/kitchen-orders.html', {'orders': orders})


def mark_order_prepared(request, pk):
    kitchen_order = KitchenOrder.objects.get(pk=pk)
    kitchen_order.is_prepared = True
    kitchen_order.prepared_at = timezone.now()
    kitchen_order.save()
    return redirect('kitchen_order_list')

