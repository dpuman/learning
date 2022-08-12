import json
from pathlib import Path
# movies = [
#     {"id": 1, "title": "Titanic", "year": 1999},
#     {"id": 2, "title": "Caital", "year": 2000}
# ]
# data = json.dumps(movies)
# # print(data)

# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[1])
print(movies[1]["title"])
