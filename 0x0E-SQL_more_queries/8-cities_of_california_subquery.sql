-- lists all the cities of Carlifornia found in hbtn_0d_usa
SELECT name FROM cities
WHERE (
	SELECT id FROM states
	WHERE name = "California"

)
ORDER BY cities.id ASC;
