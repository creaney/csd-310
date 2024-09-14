import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Foxglove1@#",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    # Query 1
    cursor1 = db.cursor()
    print("-- DISPLAYING Studio RECORDS --")
    query1 = ("SELECT studio_id, studio_name FROM studio")
    cursor1.execute(query1)
    query1Result = cursor1.fetchall()
    for result in query1Result:
        print("Studio ID: {}\nStudio Name: {}\n".format(result[0], result[1]))
    print("\n")

    # Query 2
    cursor2 = db.cursor()
    print("-- DISPLAYING Genre RECORDS --")
    query2 = ("SELECT genre_id, genre_name FROM genre")
    cursor2.execute(query2)
    query2Result = cursor2.fetchall()
    for result in query2Result:
        print("Genre ID: {}\nGenre Name: {}\n".format(result[0], result[1]))
    print("\n")

    # Query 3
    cursor3 = db.cursor()
    print("-- DISPLAYING Short Film RECORDS --")
    query3 = ("SELECT film_name, film_runtime from movies.film WHERE film_runtime < 120")
    cursor3.execute(query3)
    query3Result = cursor3.fetchall()
    for result in query3Result:
        print("Film Name: {}\nRuntime: {}\n".format(result[0], result[1]))
    print("\n")

    # Query 4
    cursor4 = db.cursor()
    print("-- DISPLAYING Director RECORDS in Order --")
    query4 = ("SELECT film_name, film_director FROM movies.film GROUP BY film_name, film_director ORDER BY film_director")
    cursor4.execute(query4)
    query4Result = cursor4.fetchall()
    for result in query4Result:
        print("Film Name: {}\nDirector: {}\n".format(result[0], result[1]))
    print("\n")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()