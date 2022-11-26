import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:

	cursor = db.cursor()
	# Displaying the fields in the studio table
	cursor.execute("SELECT studio_id, studio_name FROM studio")
	studio = cursor.fetchall()
	print("\n\n-- DISPLAYING Studio RECORDS --")
	for studio in studio:
   		print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

	# Displaying the fields in the genre table
	cursor.execute("SELECT genre_id, genre_name FROM genre")
	genre = cursor.fetchall()
	print("\n-- DISPLAYING Genre RECORDS --")
	for genre in genre:
		print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

	# Displaying the names of movies and runtimes for runtimes < 2 hours
	cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
	film = cursor.fetchall()
	print("\n-- DISPLAYING Short Film RECORDS --")
	for film in film:
		print("Film Name: {}\nFilm Runtime: {}\n".format(film[0], film[1]))

	# Displaying Director records in order of directors
	cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
	film = cursor.fetchall()
	print("\n-- DISPLAYING Director RECORDS in Order --")
	for film in film:
		print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))
db.close()
