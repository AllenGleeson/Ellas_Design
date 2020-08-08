from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products, name='products'),
    path('<int:product_id>/', views.view_product, name='view_product'),
]