from django.shortcuts import get_object_or_404, redirect, render
from .forms import LoginForm, category_create_form, product_create_form,customer_create_form,order_create_form,order_product_create_form,order_product
from .models import Category,Product,order,customer
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.db.models import Sum

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
    selected_customer = customer.objects.filter(id=customer_id).first()
    selected_customer.is_customer = True
    selected_customer.save()
    get_category = Category.objects.all().order_by('sequence').values()
    products = Product.objects.all().order_by('sequence').values()
    return render(request, 'home/product-index.html', {'categories': get_category,'products': products,'selected_customer': selected_customer})

def index_by_category(request, customer_id, category_id):
    print(customer_id)
    categories = Category.objects.all().order_by('sequence').values()
    selected_customer = get_object_or_404(customer, pk=customer_id)
    if category_id is not None:
        products = Product.objects.filter(category_id= category_id).order_by('sequence').values()
        return render(request, 'home/product-index.html', {'products': products,'categories': categories,'selected_customer': selected_customer})
    products = Product.objects.all().order_by('sequence').values()
    return render(request, 'home/product-index.html', {'products': products,'categories': categories,'selected_customer': selected_customer}) 

# Sepet Sınıfı
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}
        self.cart[product_id]["quantity"] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session["cart"] = {}
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values())
    
def cart_add(request, product_id, customer_id=None):
    product = get_object_or_404(Product, id=product_id)
    select_customer = get_object_or_404(customer, id= customer_id)
    current_order = order.objects.filter(customer=select_customer, status='pending').first()
    if current_order:
        create_order_product = order_product.objects.create(order=current_order, product=product, quantity=1, price=product.price, customer=select_customer, status='pending')
        return cart_detail(request, customer_id) 
    create_order = order.objects.create(customer=select_customer, total_price=product.price, status='pending')
    create_order_product = order_product.objects.create(order=create_order, product=product, quantity=1, price=product.price, customer=select_customer, status='pending')
    return cart_detail(request, customer_id)  # sepeti görmek için yönlendirme

def cart_detail(request, customer_id=None):
    order_product_list = order_product.objects.filter(customer_id=customer_id, status='pending').order_by('created_at').select_related('product')
    cart_total_price = order_product_list.aggregate(total_price=Sum('price'))['total_price']

    return render(request, 'cart/cart-detail.html', {
        'cart_items': order_product_list,
        'total_price': cart_total_price,
        'customer_id': customer_id,
    })

def shop_view(request):
    products = Product.objects.all()
    return render(request, 'home/shop.html', {'products': products})

# Sepetten Siparişe Dönüştürme
def cart_checkout(request, customer_id=None):
    current_order = order.objects.filter(customer_id=customer_id, status='pending').first()
    if current_order:
        current_order.status = 'completed'
        current_order.save()
    order_product_list = order_product.objects.filter(customer_id=customer_id).update(status='completed')
    current_customer = customer.objects.filter(id=customer_id).update(is_customer=False)
    return index(request,None)

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')
