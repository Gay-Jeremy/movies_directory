import os
import csv

CSV_FILE_PATH = "film.csv"
FIELD_NAMES = ['titre', 'année', 'genre', 'vu']

def save_csv(data):
    """Cette fonction enregistre le dictionnaire 'data' dans le CSV configuré dans 'CSV_FILE_PATH'
    **Attention : Cette fonction écrase le contenu du CSV existant
    """
    formatted_data = []
    for movie in data :
        formatted_data.append({
            'titre' : movie['titre'],
            'année' : int(movie['année']),
            'genre' : movie['genre'],
            'vu' : 'oui' if movie['vu'] else 'non'
        })
    with open(CSV_FILE_PATH, "w", encoding="utf-8") as file:
            writer=csv.DictWriter(file, fieldnames=FIELD_NAMES)
            writer.writeheader()
            writer.writerows(formatted_data)



def load_csv():
    """
    Cette fonction va lire le fichier CSV et retourner son contenu sous forme d'une liste de dictionnaire
    """
    if not os.path.exists(CSV_FILE_PATH):
        return[]
    data = []
    with open(CSV_FILE_PATH, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for movie in reader :
            data.append({
                'titre' : movie['titre'],
                'année' : int(movie['année']),
                'genre' : movie['genre'],
                'vu' : movie['vu'] == 'oui'
            })
        return data
    data = []


