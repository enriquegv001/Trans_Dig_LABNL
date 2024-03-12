import psycopg2 

# Replace with your actual connection details
db_params = {
    "host": "db-postgresql-sfo3-52325-do-user-15927778-0.c.db.ondigitalocean.com",
    "port": 25060,
    "dbname": "db-postgresql-sfo3-52325",
    "user": "doadmin",
    "password": "AVNS_HddN1rkSi6rAze0TdG_",
    "sslmode": "require",
    "sslrootcert": "C:/Users/Enrique/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Documents/Education/ITESM/24FJ/Transf_Dig/Trans_Dig_LABNL/3rd_app/ca-certificate.crt",
}

try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Execute SQL queries here (e.g., SELECT, INSERT, UPDATE)

    conn.commit()
    cursor.close()
    conn.close()
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")


