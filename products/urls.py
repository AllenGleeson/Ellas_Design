from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products, name='products'),
    path('<int:product_id>/', views.view_product, name='view_product'),

    path('product_management/', views.product_management,
         name='product_management'),
    path('create_product/', views.create_product, name='create_product'),
    path('create_category/', views.create_category, name='create_category'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
