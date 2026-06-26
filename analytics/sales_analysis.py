import pandas as pd
from db.connection import get_connection

def sales_by_product():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            p.product_name,
            SUM(d.quantity) AS total_sold
        FROM product p
        JOIN invoice_detail d
            ON p.product_id = d.product_id
        GROUP BY p.product_name
    """)

    df = pd.DataFrame(
        cursor.fetchall(),
        columns=[column[0] for column in cursor.description]
    )

    df.to_csv(
        "reports/products.csv",
        index=False
    )

    cursor.close()
    connection.close()

    return df