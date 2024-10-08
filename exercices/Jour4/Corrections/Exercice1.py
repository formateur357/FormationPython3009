import requests
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


def plot_publications_per_year(df):
    """
    Affiche un graphique du nombre de publications par année.

    Args:
        df (pd.DataFrame): DataFrame contenant les données des publications.
    """
    pub_per_year = df["year"].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=pub_per_year.index.astype(int), y=pub_per_year.values, palette="viridis"
    )
    plt.title("Nombre de publications par année")
    plt.xlabel("Année")
    plt.ylabel("Nombre de publications")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

"""
Explications :

- df['year'].value_counts() compte le nombre de publications par année.
- sort_index() trie les années dans l'ordre croissant.
- astype(int) convertit les années en entiers pour l'affichage.
"""


def plot_top_authors(df):
    """
    Affiche un graphique des 10 auteurs les plus prolifiques.

    Args:
        df (pd.DataFrame): DataFrame contenant les données des publications.
    """
    all_authors = df["authors"].explode()
    top_authors = all_authors.value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_authors.values, y=top_authors.index, palette="magma")
    plt.title("Top 10 des auteurs les plus prolifiques")
    plt.xlabel("Nombre de publications")
    plt.ylabel("Auteurs")
    plt.tight_layout()
    plt.show()

"""
Explications :

- df['authors'].explode() transforme les listes d'auteurs en une série avec un auteur par ligne.
- value_counts() compte le nombre d'occurrences de chaque auteur.
"""


def plot_fields_of_study(df):
    """
    Affiche un graphique des 10 champs de recherche les plus fréquents.

    Args:
        df (pd.DataFrame): DataFrame contenant les données des publications.
    """
    all_fields = df["fields_of_study"].explode()
    top_fields = all_fields.value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_fields.values, y=top_fields.index, palette="cool")
    plt.title("Top 10 des champs de recherche")
    plt.xlabel("Nombre de publications")
    plt.ylabel("Champs de recherche")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    keyword = input("Entrez un mot-clé pour la recherche de publications : ")
    works = search_works_paginated(keyword, max_results=1000)
    if works:
        df = process_data(works)
        print(f"Nombre total de publications récupérées : {len(df)}")
        # Afficher les premières lignes du DataFrame
        print(df.head())

        # Analyse et visualisation
        plot_publications_per_year(df)
        plot_top_authors(df)
        plot_fields_of_study(df)
    else:
        print("Aucune publication n'a été trouvée.")


"""
Explications supplémentaires :

. Gestion du curseur pour la pagination :

- next_cursor = '*' initialise le curseur.
- params['cursor'] = next_cursor ajoute le curseur aux paramètres.
- next_cursor = data['meta']['next_cursor'] met à jour le curseur pour la prochaine itération.

. Gestion des valeurs manquantes :

- Utilisation de dropna() pour exclure les valeurs manquantes lors des comptages.
"""
