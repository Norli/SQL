import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("""select distinct p.city, p.population, r.region 
				from population p, regions r
				where p.city = r.city
				order by p.city asc""")
	rows = c.fetchall()
	for r in rows:
		print "City: " + r[0]
		print "Population: " + str(r[1])
		print "Region: " + r[2]
		print
	 	
