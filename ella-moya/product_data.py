import json
import os
from decimal import Decimal
from typing import List, Dict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)


class ProductStorage:
    """Simple file-based storage for products"""
    
    @staticmethod
    def _get_file_path(filename: str) -> str:
        return os.path.join(DATA_DIR, filename)
    
    @staticmethod
    def load_products() -> List[Dict]:
        """Load products from JSON file"""
        file_path = ProductStorage._get_file_path('products.json')
        if not os.path.exists(file_path):
            return []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    @staticmethod
    def load_categories() -> List[Dict]:
        """Load categories from JSON file"""
        file_path = ProductStorage._get_file_path('categories.json')
        if not os.path.exists(file_path):
            return []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []


class Product:
    """Simple Product class for display"""
    
    def __init__(self, data: Dict, categories: List[Dict]):
        self.id = data.get('id')
        self.name = data.get('name', '')
        self.description = data.get('description', '')
        self.price = Decimal(str(data.get('price', 0)))
        self.image = data.get('image', '')
        self.sku = data.get('sku', '')
        category_id = data.get('category_id')
        self.category = None
        for cat in categories:
            if cat.get('id') == category_id:
                self.category = type('Category', (), {
                    'id': cat.get('id'),
                    'name': cat.get('name', ''),
                    'friendly_name': cat.get('friendly_name', cat.get('name', ''))
                })()
                break
    
    @property
    def pk(self):
        return self.id


def get_all_products():
    """Get all products as objects"""
    products_data = ProductStorage.load_products()
    categories_data = ProductStorage.load_categories()
    return [Product(p, categories_data) for p in products_data]


def get_product_by_id(product_id: int):
    """Get a single product by ID"""
    products = get_all_products()
    for product in products:
        if product.id == product_id:
            return product
    return None


def get_all_categories():
    """Get all categories"""
    categories_data = ProductStorage.load_categories()
    return [
        type('Category', (), {
            'id': c.get('id'),
            'name': c.get('name', ''),
            'friendly_name': c.get('friendly_name', c.get('name', ''))
        })()
        for c in categories_data
    ]

