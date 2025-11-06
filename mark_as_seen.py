from utilities.csvmanager import load_csv, save_csv

def mark_as_seen():
    movies = load_csv()
    query = input("Entrez le titre du film à marquer comme vu : ").strip()

    for movie in movies:
        if query.lower() == movie['titre'].lower():
            movie['vu'] = True
            print(f"Le film '{movie['titre']}' a été marqué comme vu.")

    save_csv(movies)