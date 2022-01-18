import json
import psycopg2

# ------ Read and store json data ------

f = open('test.json', 'r')
jsonf = f.read()
res = json.loads(jsonf)

# ------ Connect to database ------

PSQL = 'host=localhost port=5432 user=postgres password= dbname='
conn = psycopg2.connect(PSQL)
cur = conn.cursor()

# ------ Insert all data ------

QUERY = 'INSERT INTO jsonf(id_external, name, email) VALUES (%s, %s, %s)'

for row in res:
    id_external = row['id']
    name = row['name']
    email = row['email']

    cur.execute(QUERY, (id_external, name, email))
    conn.commit()

cur.close()
conn.close()
