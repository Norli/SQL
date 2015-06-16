import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("""select p.city, p.population, r.region from population p, regions r
				 where p.city = r.city""")
	rows = c.fetchall()
	
	for r in rows:
		print r[0], r[1], r[2] 
