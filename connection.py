import oracledb

def get_conection():
     
    return oracledb.connect(
        user="TAREAS",
        password="Javialvizu77",
        host="192.168.1.135",
        port=1521,
        service_name="XEPDB1"

    )

print(get_conection)