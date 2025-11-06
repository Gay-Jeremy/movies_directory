from utilities.csvmanager import load_csv, save_csv

def delete_movie():
    movies= load_csv()
    query = input("Entrez le titre du film à supprimer : ").strip().lower()

    for movie in movies.copy():
        if query == movie['titre'].lower():
            movies.remove(movie)
            print(f"Le film '{movie['titre']}' a été supprimé de la liste.")
    
    save_csv(movies)