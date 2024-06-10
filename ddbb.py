import psycopg2

# Datos de conexion
db_host = '127.0.0.1'
db_port = 5432
db_user = 'postgres'
db_pass = '1234'
db_name = 'dbsaurios'

def get_db_connection():
    db_connection = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_pass,
        host=db_host,
        port=db_port,
        client_encoding = 'UTF8'
    )
    return db_connection

def createSaurio(jsonsaurio):
    connection = None
    try:
        connection = get_db_connection()
        if not connection:
            return False
        cursor = connection.cursor()

        query = """INSERT INTO dinosaurios(nombresaurio, poder, dinoage, alimentacion) 
                   VALUES(%(nombreSaurio)s, %(poder)s, %(dinoAge)s, %(alimentacion)s)"""
        cursor.execute(query, jsonsaurio)
        connection.commit()
        if cursor.rowcount > 0:
            return True

    except Exception as e:
        print("Error al insertar dino")
        raise e

    finally:
        if connection is not None:
            connection.close()