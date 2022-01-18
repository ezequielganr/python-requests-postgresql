import requests
import psycopg2

# ------ Get data from api ------

URL_API = 'https://jsonplaceholder.typicode.com/users'

r = requests.get(URL_API)
r.text
res = r.json()

# ------ Connect to database ------

PSQL = 'host=localhost port=5432 user=postgres password= dbname='
conn = psycopg2.connect(PSQL)
cur = conn.cursor()

# ------ Insert all data ------

QUERY = 'INSERT INTO jsonplaceholder(id_external, name, email, street, city) VALUES (%s, %s, %s, %s, %s)'

for row in res:
    id_external = row['id']
    name = row['name']
    email = row['email']
    street = row['address']['street']
    city = row['address']['city']

    cur.execute(QUERY, (id_external, name, email, street, city))
    conn.commit()

cur.close()
conn.close()
