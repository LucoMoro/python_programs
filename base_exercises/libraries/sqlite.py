import sqlite3
import json
from pathlib import Path


#PRINT DATA ON DATABASE
#movies = json.loads(Path("movies.json").read_text())


#with sqlite3.connect("db.sqlite3") as conn:
 #   command = "INSERT INTO Movies VALUES(?, ?, ?)"
 #   for movie in movies:
   #     conn.execute(command, tuple(movie.values()))
 #   conn.commit()

#READ DATA FROM DATABASE
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies "
    cursor = conn.execute(command) #cursos is an iterable object
   # for row in cursor:
    #    print(row)
    movies = cursor.fetchall()
    print(movies)
