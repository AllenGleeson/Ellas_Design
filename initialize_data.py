"""
Initialize data files from fixtures for frontend showcase
Run this script to convert existing fixtures to JSON data files
"""
import json
import os

# Read existing fixtures
try:
    with open('products/fixtures/products.json', 'r') as f:
        products_fixture = json.load(f)
except FileNotFoundError:
    print("ERROR: products/fixtures/products.json not found")
    products_fixture = []

try:
    with open('products/fixtures/categories.json', 'r') as f:
        categories_fixture = json.load(f)
except FileNotFoundError:
    print("ERROR: products/fixtures/categories.json not found")
    categories_fixture = []

# Create data directory
os.makedirs('data', exist_ok=True)

# Convert categories
categories = []
for item in categories_fixture:
    categories.append({
        'id': item['pk'],
        'name': item['fields']['name'],
        'friendly_name': item['fields']['friendly_name']
    })

with open('data/categories.json', 'w') as f:
    json.dump(categories, f, indent=2)

print(f"Created data/categories.json with {len(categories)} categories")

# Convert products
products = []
for item in products_fixture:
    products.append({
        'id': item['pk'],
        'category_id': item['fields']['category'],
        'sku': item['fields'].get('sku', ''),
        'name': item['fields']['name'],
        'description': item['fields']['description'],
        'price': str(item['fields']['price']),
        'image': item['fields'].get('image', '')
    })

with open('data/products.json', 'w') as f:
    json.dump(products, f, indent=2)

print(f"Created data/products.json with {len(products)} products")
print("\nData files initialized successfully!")
print("Files created in 'data/' directory:")

