"""from services.product_service import get_products

products = get_products()

for product in products:
    print(product)"""

"""from analytics.sales_analysis import sales_by_product

data = sales_by_product()

for row in data:
    print(row)"""

from analytics.sales_analysis import sales_by_product

df = sales_by_product()

print(df)