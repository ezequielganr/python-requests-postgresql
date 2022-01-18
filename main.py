import psycopg2

# ------ Connect to database ------

PSQL = 'host=localhost port=5432 user=postgres password= dbname='
conn = psycopg2.connect(PSQL)
cur = conn.cursor()

# ------ Get all data ------

cur.execute('SELECT * FROM main')
res = cur.fetchall()
cur.close()
conn.close()

# ------ Connect to the backup database ------

PSQL_BACKUP = 'host=localhost port=5432 user=postgres password= dbname='
conn_backup = psycopg2.connect(PSQL_BACKUP)
cur_backup = conn_backup.cursor()

# ------ Insert all data ------

QUERY = 'INSERT INTO backup(id_external, name, email) VALUES (%s, %s, %s)'

for row in res:
    id_external = row[0]
    name = row[1]
    email = row[2]

    cur_backup.execute(QUERY, (id_external, name, email))
    conn_backup.commit()

cur_backup.close()
conn_backup.close()
