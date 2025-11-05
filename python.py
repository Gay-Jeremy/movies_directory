import csv
import os
# =====================================================================================================







reponse = 0
while reponse != "6" :


    menu_affichage = {"1." : "Ajouter Film",
        "2." : "Afficher Film",
        "3." : "Rechercher Film",
        "4." : "Supprimer Film",
        "5." : "Marquer comme vu",
        "6." : "Quitter"
    }

    for cle, valeur in menu_affichage.items() :
        print(cle, valeur)

    reponse = input("Que souhaitez-vous faire ? : ")

    menu(reponse)





