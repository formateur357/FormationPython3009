import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def search_works_paginated(keyword, max_results=1000):
    base_url = "https://api.openalex.org/works"
    params = {
        "filter": f"title.search:{keyword}",
        "per-page": 200,
        "mailto": "votre_email@example.com",
        "cursor": "*",
    }
    results = []
    count = 0
    while True:
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print(f"Erreur lors de la requête : {response.status_code}")
            break
        data = response.json()
        results.extend(data["results"])
        count = len(results)
        print(f"Récupération de {count} publications...")
        # Vérifier si 'next_cursor' est présent
        if "next_cursor" in data["meta"]:
            params["cursor"] = data["meta"]["next_cursor"]
        else:
            break  # Plus de pages à récupérer
        if count >= max_results:
            break  # Limite de résultats atteinte
    return results[:max_results]

"""
Explications :

Paramètres de la requête :

- filter: Filtre la recherche en utilisant le mot-clé dans le titre des publications.
- per-page: Nombre de résultats par page (maximum 200).
- mailto: Votre adresse e-mail pour identifier le trafic.

Pagination :

- Utilise le curseur next pour récupérer les pages suivantes.
- Continue à récupérer les résultats jusqu'à ce que le nombre maximum soit atteint ou qu'il n'y ait plus de pages.
"""


def process_data(works):
    """
    Traite les données des publications pour extraire les informations clés.

    Args:
        works (list): Liste des publications.

    Returns:
        pd.DataFrame: DataFrame contenant les données traitées.
    """
    records = []
    for work in works:
        # Gestion des valeurs manquantes avec get()
        record = {
            "title": work.get("title"),
            "publication_date": work.get("publication_date"),
            "year": work.get("publication_year"),
            "authors": [
                author["author"]["display_name"]
                for author in work.get("authorships", [])
            ],
            "journal": work.get("host_venue", {}).get("display_name"),
            "citations_count": work.get("cited_by_count"),
            "fields_of_study": [
                concept["display_name"]
                for concept in work.get("concepts", [])
                if concept.get("score", 0) >= 0.5
            ],
        }
        records.append(record)
    df = pd.DataFrame(records)
    return df

"""
Explications :

. Extraction des informations :
  - Titre (title)
  - Date de publication (publication_date)
  - Année de publication (year)
  - Auteurs (authors): Liste des noms des auteurs.
  - Journal (journal): Nom de la revue ou du journal.
  - Nombre de citations (citations_count)
  - Champs de recherche (fields_of_study): Concepts associés à la publication
    avec un score >= 0.5 (pour filtrer les concepts les plus pertinents).
"""


def plot_publications_per_year(df, keyword):
    pub_per_year = df["year"].dropna().value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=pub_per_year.index.astype(int), y=pub_per_year.values, palette="viridis"
    )
    plt.title("Nombre de publications par année")
    plt.xlabel("Année")
    plt.ylabel("Nombre de publications")
    plt.xticks(rotation=45)
    plt.tight_layout()
    image_path = os.path.join("static", "images", f"pub_per_year_{keyword}.png")
    plt.savefig(image_path)
    plt.close()
    return image_path


def plot_top_authors(df, keyword):
    all_authors = df["authors"].explode().dropna()
    top_authors = all_authors.value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_authors.values, y=top_authors.index, palette="magma")
    plt.title("Top 10 des auteurs les plus prolifiques")
    plt.xlabel("Nombre de publications")
    plt.ylabel("Auteurs")
    plt.tight_layout()
    image_path = os.path.join("static", "images", f"top_authors_{keyword}.png")
    plt.savefig(image_path)
    plt.close()
    return image_path


def plot_fields_of_study(df, keyword):
    all_fields = df["fields_of_study"].explode().dropna()
    top_fields = all_fields.value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_fields.values, y=top_fields.index, palette="cool")
    plt.title("Top 10 des champs de recherche")
    plt.xlabel("Nombre de publications")
    plt.ylabel("Champs de recherche")
    plt.tight_layout()
    image_path = os.path.join("static", "images", f"fields_of_study_{keyword}.png")
    plt.savefig(image_path)
    plt.close()
    return image_path
