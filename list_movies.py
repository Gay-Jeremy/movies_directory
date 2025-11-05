from utilities.csvmanager import load_csv

def list_movies():
    movies = load_csv()

    print("🍿 Les films enregistrés :")

    for movie in movies :
        print(f"->{movie['titre']} {movie['année']} {movie['genre']} {movie['vu']} ")