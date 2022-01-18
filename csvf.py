import psycopg2
import csv

# ------ Read and store csv data ------

f = open('people.csv', encoding='utf-8')
csvf = csv.DictReader(f)

# ------ Connect to database ------

PSQL = 'host=localhost port=5432 user=postgres password= dbname='
conn = psycopg2.connect(PSQL)
cur = conn.cursor()

# ------ Insert all data ------

QUERY = 'INSERT INTO csvf(id_external, name, email) VALUES (%s, %s, %s)'

for row in csvf:
    id_external = row['id']
    name = row['name']
    email = row['email']

    cur.execute(QUERY, (id_external, name, email))
    conn.commit()

cur.close()
conn.close()
