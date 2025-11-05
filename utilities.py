


def menu(reponse) :
    if reponse == "1" :
        ajouter_film()
    if reponse == "2" :
        afficher_film()
    if reponse == "3" :
        rechercher_film()
    if reponse == "4" :
        supprimer_film()
    if reponse == "5" :
        marquer_comme_vu()
    else :
        pass

# =====================================================================================================

def ajouter_film():
    """
    Ajoute un film au fichier film.csv
    """

    titre = input("Quel est le titre du film ? : ").lower().capitalize()
    annee = input(f"Quelle est l'année de sortie du film {titre} ? : ")
    genre = input(f"Quel est le genre du film {titre} ? : ")
    vu = input(f"Avez-vous déjà visionné {titre} ? : ")

    film = {'titre': titre, 'année': annee, 'genre': genre, 'vu': vu}

    # Teste l'existence du fichier csv
    file_exists = os.path.isfile('film.csv')

    with open('film.csv', 'a', encoding='utf-8', newline='') as file:
        fieldnames = ['titre', 'année', 'genre', 'vu']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Écrire l'en-tête seulement si le fichier n'existe pas
        if not file_exists:
            writer.writeheader()
        # Écrire un seul film
        writer.writerow(film) 
    print(f"Le film {titre} a été ajouté avec succès !")

# =====================================================================================================

def afficher_film() :
    """
    Affiche les films présent dans film.csv
    """

    with open('film.csv', mode='r', encoding ='utf-8', newline='') as file :
        reader = csv.DictReader(file)
        rows = list(reader)
    for dic in rows :
        print("===============================")
        print(f" Titre : {dic['titre']}")
        print(f" Année : {dic['année']}")
        print(f" Genre : {dic['genre']}")
        print(f" Déjà vu : {dic['vu']}")
        print("===============================")

# =====================================================================================================

def rechercher_film() :
    """
    Recherche si un films est présent dans film.csv si non => ajout 
    """

    film_recherche = input("Quel film souhaitez-vous rechercher ? : ").lower().capitalize()
    with open('film.csv', mode='r', encoding ='utf-8', newline='') as file :
        reader = csv.DictReader(file)
        rows = list(reader)
    boucle = "False"
    for dic in rows :   
        if film_recherche in dic['titre'] :
            print(f"Voici les informations pour le film {film_recherche} : ")
            print(f"Année : {dic['année']}")
            print(f"genre : {dic['genre']}")
            print(f"Déjà visionné : {dic['vu']}")
    boucle = "True"

    if boucle == "True" : 
        print(f"Le film {film_recherche} n'existe pas dans le fichier film.csv")
        reponse_recherche = input("Souhaitez-vous l'ajouter (O/N) ?")
        if reponse_recherche.upper() == "O" :
            ajouter_film()

# =====================================================================================================

def supprimer_film() :
    """
    Supprime un film de film.csv
    """

    film_supprime = input("Quel film souhaitez-vous supprimer ? : ").lower().capitalize()

    with open('film.csv', mode = 'r', encoding='utf-8', newline = '') as file :
        reader = csv.DictReader(file)
        #filtre le fichier 
        lignes = [row for row in reader if row['titre'] != film_supprime]

    with open('film.csv', 'w', encoding='utf-8', newline='') as file:
                field = ['titre', 'année', 'genre', 'vu']
                writer=csv.DictWriter(file, fieldnames=field)
                writer.writeheader()
                writer.writerows(lignes)
    print(f"{film_supprime} a été supprimé avec succès !")

# =====================================================================================================

def marquer_comme_vu() :
    """
    Marque comme vu un film dans film.csv
    """

    film_vu = input("Quel film souhaitez-vous marquer comme vu ? : ").lower().capitalize()
    with open('film.csv', mode = 'r', encoding = 'utf-8', newline = '') as file :
        reader = csv.DictReader(file)
        rows = list(reader)
    for dic in rows :
        if film_vu in dic['titre'] :
            dic['vu']='oui'
    print(rows)

    with open('film.csv', mode = 'w', encoding = 'utf-8', newline = '' ) as file :
        field = ['titre', 'année', 'genre', 'vu']
        writer = csv.DictWriter(file, fieldnames=field)
        writer.writeheader()
        writer.writerows(rows)

# =====================================================================================================