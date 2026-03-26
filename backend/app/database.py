import psycopg2

def get_db():
    return psycopg2.connect(
        host="db",
        database="inventory",
        user="postgres",
        password="postgres"
    )
