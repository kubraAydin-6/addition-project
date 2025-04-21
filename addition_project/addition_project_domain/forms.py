from django import forms
from .models import Category

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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'sequence': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        },
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