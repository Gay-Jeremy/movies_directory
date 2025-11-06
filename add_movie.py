from utilities.csvmanager import load_csv, save_csv

def add_movie():
    title = input("Entrez le titre du film: ").strip().capitalize() or "n/a"
    year = input("Entrez l'année: ") 
    genre = input("Entrez le genre: ") or "n/a"
    seen = input("L'avez-vous vu ? [o/N] ").strip().lower() == "O"

    if year and year.isdigit():
        year = int(year)
    else :
        year = 0

    if seen == "O" or seen == "o":
        seen = 'Oui'
    else:
        seen = 'Non'

    existing_movies = load_csv()
    existing_movies.append ({
        'titre' : title,
        'année' : year,
        'genre' : genre,
        'vu' : seen
    })

    save_csv(existing_movies)
    print(f"Votre filmothèque a été sauvegardé ! {title} a été ajouté.")

