from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sümbok", views.create_category, name="create_category"),
    path("sümbok/ürün", views.create_product, name="create_product"),
    path("sümbok/müşteri", views.create_customer, name="create_customer"),
    path("sümbok/sipariş", views.create_order, name="create_order"),
    path("sümbok/sipariş/ürün", views.create_order_product, name="create_order_product"),
    path("<int:category_id>/", views.index, name="index_by_category")
]
