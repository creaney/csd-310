import mysql.connector
from mysql.connector import errorcode

def show_films(cursor, title):
    #   method to execute an inner join on all tables,
    #       iterate over the dataset and output the results to the terminal window

    #   inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON "
                   "film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    #   get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    #   iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

config = {
    "user": "root",
    "password": "Foxglove1@#",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    # Display Films
    cursor1 = db.cursor()
    show_films(cursor1, "DISPLAYING FILMS")

    # Insert 'The Maze Runner' into film table
    cursor2 = db.cursor()
    query2 = ("INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)"
              " VALUES (4, 'The Maze Runner', 2014, 113, 'Wes Ball', 1, 2)")
    cursor2.execute(query2)

    # Display Films after insert
    cursor3 = db.cursor()
    show_films(cursor3, "DISPLAYING FILMS AFTER INSERT")

    # Update Alien to be a Horror film
    cursor4 = db.cursor()
    query4 = ("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")
    cursor4.execute(query4)

    # Display Films after updating Alien to be a Horror film
    cursor5 = db.cursor()
    show_films(cursor5, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete the movie Gladiators from db
    cursor6 = db.cursor()
    query6 = ("DELETE FROM film WHERE film_name = 'Gladiator'")
    cursor6.execute(query6)

    # Display Films after delete
    cursor7 = db.cursor()
    show_films(cursor7, "DISPLAYING FILMS AFTER DELETE")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()