import pandas as pd
import matplotlib.pyplot as mpl


# Creation d'un dataframe a partir d'un dictionnaire
data = {
    "Annee": [2020, 2021, 2022, 2023],
    "Ventes": [150, 200, 250, 300],
    "Couts": [100, 120, 180, 220],
}

df = pd.DataFrame(data)

# Tracer un graphique des ventes
mpl.figure(figsize=(10, 5)) # definir la taille de la figure
mpl.plot(df['Annee'], df['Ventes'], marker='o', color='b', label='Ventes') # Tracer les ventes
mpl.plot(df['Annee'], df['Couts'], marker='o', color='r', label='Couts') # Tracer les couts
mpl.title("Ventes et Couts par Annee") # Titre du graphique
mpl.xlabel('Annee') # Etiquette de l'axe X
mpl.ylabel("Montant")  # Etiquette de l'axe y
mpl.legend()   # Afficher la legende
mpl.grid() # Affiche la grille
mpl.show() # Affiche le graphique
