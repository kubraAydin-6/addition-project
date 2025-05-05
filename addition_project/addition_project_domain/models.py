from django.db import models

class base_model(models.Model):
    """
    Base model for all aggregate roots in the application.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    class Meta:
        abstract = True

class Category(base_model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class customer(base_model):
    name = models.CharField(max_length=255)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class order_product(base_model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_products') #fiş
    product = models.ForeignKey('Product', on_delete=models.CASCADE) #ürün
    quantity = models.PositiveIntegerField(default=1) #ürün miktarı
    price = models.DecimalField(max_digits=10, decimal_places=2)# ürün fiyatı
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='order_products')# müşteri
    status = models.CharField(max_length=50, choices=[('pending', 'bekliyor'), ('completed', 'tamamlandı'), ('canceled', 'iptal edildi')])# sipariş durumu

    def __str__(self):
        return f"{self.product.name} - {self.quantity} pcs"

    class Meta:
        verbose_name = 'Order Product'
        verbose_name_plural = 'Order Products'
    
class order(base_model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)# müşteri
    total_price = models.DecimalField(max_digits=10, decimal_places=2)# toplam fiyat
    status = models.CharField(max_length=50, choices=[('pending', 'ödeme bekliyor'), ('completed', 'ödendi'), ('canceled', 'iptal edildi')])# sipariş durumu

class Product(base_model):#ürün(körili makarna) çeşidi
    name = models.CharField(max_length=255)#"ürün adı"
    description = models.TextField(blank=True, null=True)#"ürün açıklaması"
    price = models.DecimalField(max_digits=10, decimal_places=2)# fiyatı
    image_url = models.URLField(max_length=255, blank=True, null=True)# resim url'si
    category = models.ForeignKey('Category', on_delete=models.CASCADE)# kategori
    sequence = models.IntegerField(default=0)# sıralama

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
class KitchenOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    is_prepared = models.BooleanField(default=False)
    prepared_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.order} - {'Hazır' if self.is_prepared else 'Hazırlanıyor'}"