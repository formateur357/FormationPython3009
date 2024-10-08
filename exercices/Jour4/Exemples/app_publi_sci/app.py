import requests
import json
import ast
from flask import Flask, render_template, request, redirect, url_for

from openAlexApi import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if requests.method == "POST":
        keyword = requests.form["keyword"].strip()
        if not keyword:
            error = "Veuillez entrer un mot-clé."
            return render_template("index.html", error=error)

        # Nettoyer le mot-clé pour les noms de fichiers
        safe_keyword = keyword.replace(" ", "_")
        data_file = f"data_{safe_keyword}.json"
        data_path = os.path.join("data", data_file)

        # Vérifier si le fichier de données existe déjà
        if os.path.exists(data_path):
            with open(data_path, "r", encoding="utf-8") as f:
                works = json.load(f)
        else:
            works = search_works_paginated(keyword, max_results=1000)
            if works:
                # Créer le dossier 'data' s'il n'existe pas
                if not os.path.exists("data"):
                    os.makedirs("data")
                with open(data_path, "w", encoding="utf-8") as f:
                    json.dump(works, f, ensure_ascii=False, indent=4)
            else:
                error = "Aucune publication n'a été trouvée pour ce mot-clé."
                return render_template("index.html", error=error)

        df = process_data(works)

        # Convertir les colonnes contenant des listes si nécessaire
        if isinstance(df["authors"].iloc[0], str):
            df["authors"] = df["authors"].apply(ast.literal_eval)
        if isinstance(df["fields_of_study"].iloc[0], str):
            df["fields_of_study"] = df["fields_of_study"].apply(ast.literal_eval)

        # Générer les graphiques
        pub_year_image = plot_publications_per_year(df, safe_keyword)
        top_authors_image = plot_top_authors(df, safe_keyword)
        fields_of_study_image = plot_fields_of_study(df, safe_keyword)

        return render_template(
            "index.html",
            keyword=keyword,
            pub_year_image=pub_year_image,
            top_authors_image=top_authors_image,
            fields_of_study_image=fields_of_study_image,
        )
    else:
        return render_template("index.html")


"""
Explications :

- Gestion du formulaire : Si la méthode est POST, nous récupérons le mot-clé saisi par l'utilisateur.
- Vérification du mot-clé : Si le mot-clé est vide, nous affichons un message d'erreur.
- Chargement ou récupération des données : Si les données existent déjà dans un fichier, nous les chargeons ; sinon, nous les récupérons via l'API et les sauvegardons.
- Traitement des données : Nous appelons process_data() pour obtenir le DataFrame.
- Conversion des chaînes en listes : Si nécessaire, nous convertissons les colonnes authors et fields_of_study en listes.
- Génération des graphiques : Nous appelons les fonctions de visualisation et récupérons les chemins des images générées.
- Rendu du template : Nous passons les images et le mot-clé au template index.html.
"""

@app.route('/about')
def about():
  return 'Cette application fournit des publications scientifiques.'


if __name__ == '__main__':
  app.run(debug=True)
