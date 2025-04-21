from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sümüklü", views.create_category, name="create_category"),
    path("sümüklü/ürün", views.create_product, name="create_product"),
    path("sümüklü/müşteri", views.create_customer, name="create_customer"),
    path("sümüklü/sipariş", views.create_order, name="create_order"),
    path("sümüklü/sipariş/ürün", views.create_order_product, name="create_order_product"),
]
