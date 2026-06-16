from services.product_service import get_products

products = get_products()

for product in products:
    print(product)