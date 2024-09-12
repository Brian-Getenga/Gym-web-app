from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    
]
