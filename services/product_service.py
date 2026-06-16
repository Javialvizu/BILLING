from db.connection import get_connection

def get_products():
    
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
            SELECT * FROM PRODUCT
                   """)
    
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return products