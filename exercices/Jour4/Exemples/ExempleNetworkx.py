import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Créer un DataFrame avec des données de relations
data = {
    "Personne_A": ["Alice", "Alice", "Bob", "Bob", "Charlie"],
    "Personne_B": ["Bob", "Charlie", "Alice", "David", "Eve"],
}

df = pd.DataFrame(data)
print(df)

# Créer un graphe orienté
G = nx.from_pandas_edgelist(df, "Personne_A", "Personne_B", create_using=nx.DiGraph())

# Dessiner le graphe
plt.figure(figsize=(10, 6))  # Définir la taille de la figure
pos = nx.spring_layout(G)  # Positionnement des nœuds

# Tracer le graphe
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    arrows=True,
)

# Ajouter un titre
plt.title("Graphe de Données Liées")
plt.show()  # Afficher le graphique
