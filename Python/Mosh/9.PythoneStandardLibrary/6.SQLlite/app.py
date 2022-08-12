
import sqlite3
import json
from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())

# print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    # command = "INSERT INTO Movies VALUES(?,?,?)"
    # for movie in movies:
    #     conn.execute(command, tuple(movie.values()))
    # conn.commit()

    cursor = conn.execute(command)
    # for cur in cursor:
    #     print(cur)
    mov = cursor.fetchall()
    print(mov)
