import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

results = cursor.fetchall()

connection.close()

for results in results:
    print(result)