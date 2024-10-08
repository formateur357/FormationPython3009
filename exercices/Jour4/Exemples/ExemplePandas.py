import pandas as pd

# Creation d'un dataframe a partir d'un dictionnaire
data = {
  'Annee': [2020, 2021, 2022, 2023],
  'Ventes': [150, 200, 250, 300],
  'Couts': [100, 120, 180, 220]
}

df = pd.DataFrame(data)

# print(df)

# Statistiques descriptives
# print(df.describe())

# Selection d'une colonne
ventes = df['Ventes']
# print(ventes)

# Ajout d'une colonne
df['Profit'] = df['Ventes'] - df['Couts']
print(df)