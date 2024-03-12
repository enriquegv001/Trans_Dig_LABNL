import psycopg2 

# Replace with your actual connection details
db_params = {
    "host": "db-postgresql-sfo3-52325-do-user-15927778-0.c.db.ondigitalocean.com",
    "port": 25060,
    "dbname": "defaultdb",
    "user": "doadmin",
    "password": "AVNS_HddN1rkSi6rAze0TdG_",
    "sslmode": "require",
    "sslrootcert": "C:/Users/Enrique/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Documents/Education/ITESM/24FJ/Transf_Dig/Trans_Dig_LABNL/3rd_app/ca-certificate.crt",
}


# Connect to your postgres DB
conn = psycopg2.connect(**db_params)
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("""
    CREATE TABLE registros (
    dia date,
    id varchar(25)
    nombre varchar(40),
    edad serial,
    genero VARCHAR(40),
    residencia VARCHAR(40),
    cp serial,
    estudios varchar(25),
    ocupacion varchar(25),
    grupo_social varchar(25),
    actividad varchar(25),
    proyecto_labnl varchar(50),
    foto varchar(25),
    uso_datos varchar(25),
    correo varchar(25),
    recibir_info varchar(25),
    )
""")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()


"""
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Execute SQL queries here (e.g., SELECT, INSERT, UPDATE)

    conn.commit()
    cursor.close()
    conn.close()
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")
"""



