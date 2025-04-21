from django.shortcuts import redirect, render
from .forms import category_create_form
from .models import Category

def index(request):
    categories = Category.objects.all()
    return render(request, 'home/index.html', {'categories': categories})

def create_category(request):
    if request.method == "POST":
        form = category_create_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = category_create_form()
    return render(request, 'categories/create-category.html', {'form': form})