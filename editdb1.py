import sqlite3

#lag en tilkobling til databasen
with sqlite3.connect("new.db") as connection:
	#lag en peker til tilkoblingen
	c = connection.cursor()
	
	#oppdater databasen
	c.execute("update population set population = 9000000 where city = 'New York City'")
	c.execute("delete from population where city = 'Boston'")
	print "\nNEW DATA:\n"
	
	#print ut info fra databasen
	c.execute("select * from population")
	rows = c.fetchall()
	for r in rows:
		print r[0], r[1], r[2]
			
