from add_movie import add_movie
from list_movies import list_movies
from search_movies import search_movies
from mark_as_seen import mark_as_seen
from delete_movies import delete_movie  

print("Bienvenue dans votre gestionnaire de films !\n")
while True:
    print("\nQue souhaitez-vous faire ?")
    print("1. Ajouter un film")
    print("2. Lister les films")
    print("3. Rechercher un film")
    print("4. Marquer un film comme vu")
    print("5. Supprimer un film")
    print("6. Quitter")

    choice = input("Entrez le numéro de votre choix : ").strip()

    if not choice.isdigit() or int(choice) > 5 or int(choice) <= 0:
        print("Choix invalide, veuillez réessayer.")
        continue

    match choice:
        case '1':
            add_movie()
        case '2':
            list_movies()
        case '3':
            search_movies()
        case '4':
            mark_as_seen()
        case '5':
            delete_movie()
        case '6':
            print("Au revoir !")
            exit()
