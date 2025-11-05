from ..utilities.csvmanager import load_csv, save_csv

def add_movie():
    title = input("Entrez le titre du film: ").strip().capitalize() or "n/a"
    year = input("Entrez l'année: ") 
    genre = input("Entrez le genre: ") or "n/a"
    seen = input("L'avez-vous vu ? [o/N] ").strip().lower() == "O"

    if year and year.isdigit():
        year = int(year)
    else :
        year = 0

    existing_movies = load_csv()
    existing_movies.append ({
        'titre' : title,
        'année' : year,
        'genre' : genre,
        'vu' : seen
    })
    
