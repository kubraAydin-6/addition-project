from django import forms
from .models import Category, Product, customer,order, order_product

class category_create_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image_url', 'sequence', 'is_active']
        labels = {
            'name': 'Kategori Adı',
            'image_url': 'Resim URL',
            'sequence': 'Sıralama',
            'is_active': 'Aktif mi?',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kategori Adı Giriniz.'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Resim Ekleyiniz.'}),
            'sequence': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Kategori Sırası Seçiniz.'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'name': {
                'required': 'Bu alan zorunludur.',
                'max_length': 'Kategori adı 255 karakterden fazla olamaz.',
            },
            'image_url': {
                'required': 'Bu alan zorunludur.',
                'invalid': 'Geçersiz URL formatı.',
            },
            'sequence': {
                'required': 'Bu alan zorunludur.',
                'invalid': 'Geçersiz sayı formatı.',
            },
            'is_active': {
                'required': 'Bu alan zorunludur.',
            },
        }

class product_create_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image_url', 'category', 'sequence']
        labels = {
            'name': 'Ürün Adı',
            'description': 'Ürün Açıklaması',
            'price': 'Fiyat',
            'image_url': 'Resim URL',
            'category': 'Kategori',
            'sequence': 'Sıralama',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ürün Adı Giriniz.'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ürün Açıklaması Giriniz.'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ürün Fiyatı Giriniz.'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ürün Resmi Ekleyiniz.'}),
            'category': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Kategori Seçiniz.'}),
            'sequence': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ürün Sıralaması Giriniz.'}),
        }
        error_messages = {
            'name': {
                'required': 'Bu alan zorunludur.',
                'max_length': 'Ürün adı 255 karakterden fazla olamaz.',
                'min_length': 'Ürün adı 2 karakterden az olamaz.',
            },
            'description': {
                'max_length': 'Ürün açıklaması 1000 karakterden fazla olamaz.',
            },
            'price': {
                'required': 'Bu alan zorunludur.',
                'invalid': 'Geçersiz fiyat formatı.',
            },
            'image_url': {
                'required': 'Bu alan zorunludur.',
                'invalid': 'Geçersiz URL formatı.',
            },
            'category': {
                'required': 'Bu alan zorunludur.',
            },
            'sequence': {
                'required': 'Bu alan zorunludur.',
                'invalid': 'Geçersiz sayı formatı.',
            },

        }

class customer_create_form(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['name', 'is_customer']
        labels = {
            'name': 'Müşteri Adı',
            'is_customer': 'Müşteri mi?',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_customer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'name': {
                'required': 'Bu alan zorunludur.',
                'max_length': 'Müşteri adı 255 karakterden fazla olamaz.',
            },
            'is_customer': {
                'required': 'Bu alan zorunludur.',
            },
        }

class order_create_form(forms.ModelForm):
    class Meta:
        model = order
        fields = ['customer', 'total_price', 'status']
        labels = {
            'customer': 'Müşteri',
            'total_price': 'Toplam Fiyat',
            'status': 'Sipariş Durumu',
        }
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
        error_messages = {
            'customer': {
                'required': 'Bu alan zorunludur.',
            },
            'total_price': {
                'required': 'Bu alan zorunludur.',
                'invalid': 'Geçersiz fiyat formatı.',
            },
            'status': {
                'required': 'Bu alan zorunludur.',
            },
        }

class order_product_create_form(forms.ModelForm):
    class Meta:
        model = order_product
        fields = ['order', 'product', 'quantity', 'price', 'customer', 'status']
        labels = {
            'order': 'Sipariş',
            'product': 'Ürün',
            'quantity': 'Miktar',
            'price': 'Fiyat',
            'customer': 'Müşteri',
            'status': 'Sipariş Durumu',
        }
        widgets = {
            'order': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
        error_messages = {
            'order': {
                'required': 'Bu alan zorunludur.',
            },
            'product': {
                'required': 'Bu alan zorunludur.',
            },
            'quantity': {
                'required': 'Bu alan zorunludur.',
                'invalid': 'Geçersiz sayı formatı.',
            },
            'price': {
                'required': 'Bu alan zorunludur.',
                'invalid': 'Geçersiz fiyat formatı.',
            },
            'customer': {
                'required': 'Bu alan zorunludur.',
            },
            'status': {
                'required': 'Bu alan zorunludur.',
            },
        }

class LoginForm(forms.Form):
    userName = forms.CharField(label="Kullanıcı Adı", required=True)
    password = forms.CharField(label="Şifre", required=True, widget=forms.PasswordInput)

    error_messages = {
            'userName': {
                'required': 'Bu alan zorunludur.',
            },
            'password': {
                'required': 'Bu alan zorunludur.',
            }
        }