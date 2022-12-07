import json
from pathlib import Path

#WRITE IN JSON FILES
#movies = [
   # {"id": 1, "title":"Terminator", "year": 1989},
   # {"id": 2, "title":"Kindergarten", "year": 1993}
#]

#data = json.dumps(movies)
#Path("movies.json").write_text(data)

#READ FROM JSON FILES
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0]["title"])