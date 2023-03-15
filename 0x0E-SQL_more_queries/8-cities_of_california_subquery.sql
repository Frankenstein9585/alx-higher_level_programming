-- lists all the cities of Carlifornia found in hbtn_0d_usa
SELECT id, name FROM cities
WHERE state.id IN 
	(SELECT id FROM states
	WHERE name = "California")
ORDER BY cities.id ASC;
