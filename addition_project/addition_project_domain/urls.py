from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_user, name="login_user"),
    path("ui-maps", views.ui_map, name="ui_map"),
    path("ui-tables", views.ui_map, name="ui_tables"),
    path("ui-typographies", views.ui_typography, name="ui_typography"),
    path("ui-notifications", views.ui_notification, name="ui_notifications"),
    path("logout", views.logout, name="logout"),
    path("sümbok", views.create_category, name="create_category"),
    path("sümbok/ürün", views.create_product, name="create_product"),
    path("sümbok/müşteri", views.create_customer, name="create_customer"),
    path("sümbok/sipariş", views.create_order, name="create_order"),
    path("sümbok/sipariş/ürün", views.create_order_product, name="create_order_product"),
    path("<int:category_id>/", views.index, name="index_by_category"),
    path("admin/categories", views.category_list, name="category_list"),
    path("admin/products", views.product_list, name="product_list"),
    path("admin/invoices", views.invoice_list, name="invoice_list"),
    path("admin/customers", views.customer_list, name="customer_list"),
    path("sümbok/update/<int:category_id>", views.update_category, name="update_category"),
    path("sümbok/update/ürün/<int:product_id>", views.update_product, name="update_product"),
    path("sümbok/update/müşteri/<int:customer_id>", views.update_customer, name="update_customer"),
]
