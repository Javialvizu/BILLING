from db.connection import get_connection
import pandas as pd

def sales_by_product():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
                SELECT 
                   p.PRODUCT_NAME,
                   SUM(d.QUANTITY) AS TOTAL_SOLD
                FROM PRODUCT p
                JOIN INVOICE_DETAIL d
                ON p.PRODUCT_ID = d.PRODUCT_ID
                GROUP BY p.PRODUCT_NAME
                   
                   """)
    
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results

