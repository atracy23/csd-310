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

    def show_films(cursor, title):
        # method to execute an inner join on all tables,
        #   iterate over the dataset and output the results to the terminal window.

        cursor = db.cursor(cursor, title)

        # inner join query
        cursor.execute("SELECT film.film_name AS Name, film.film_director AS Director,\
         genre.genre_name AS Genre, studio.studio_name AS 'Studio Name' FROM film\
          INNER JOIN genre ON film.genre_id = genre.genre_id\
           INNER JOIN studio ON film.studio_id = studio.studio_id ORDER BY film_id")

        # get the results from the cursor object
        films = cursor.fetchall()

        print("\n  -- {} --".format(title))

        # iterate over the film data set and display the results
        for film in films:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))
        return;

    def add_films(cursor, title):
        # method to execute an add film on all tables needed,
        #   iterate over the dataset and output the results to the terminal window.

        cursor = db.cursor(cursor, title)

        # inner join query
        cursor.execute("INSERT INTO film (film_name, film_releaseDate, film_runtime,\
                 film_director, studio_id, genre_id)\
                 VALUES ('Die Hard', 1988, 82, 'John McTiernan', 1, 4)")
        return;

    def update_films(cursor, title):
        # method to execute an add film on all tables needed,
        #   iterate over the dataset and output the results to the terminal window.

        cursor = db.cursor(cursor, title)

        # inner join query
        cursor.execute("UPDATE film SET genre_id = '1' WHERE film_name = 'Alien'")
        return;

    def remove_films(cursor, title):
        # method to execute a delete film on all tables needed,
        #   iterate over the dataset and output the results to the terminal window.

        cursor = db.cursor(cursor, title)

        # inner join query
        cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
        return;

    cursor = db.cursor()

    # Printing the films
    show_films(cursor, "DISPLAYING FILMS")

    # Adding film (Die Hard)
    add_films(cursor, "ADDING FILM")

    # Printing the films after insert
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Updating films (Changing Alien to Horror Genre)
    update_films(cursor, "Updating FILM")

    # Printing the films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Deleting films (Gladiator)
    remove_films(cursor, "Deleting FILM")

    # Printing the films after deletion
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

db.close()
