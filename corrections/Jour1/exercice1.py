# Etape 1 : Demander à l'utilisateur d'entrer une phrase

phrase = input("Entrez une phrase : ")

# Etape 2 : Convertir la phrase en une liste de mots en minuscules
""" On utilise la methode split() pour separer les mots sur les espaces
Et la methode lower() pour convertir tous les caracteres en minuscules. """

mots = phrase.lower().split()

# Etape 3 : Creer un dictionnaire pour compter les occurences de chaque mot

frequence_mots = {}

# Parcourir la liste
for mot in mots:
    if mot in frequence_mots:
      frequence_mots[mot] += 1
    else:
      frequence_mots[mot] = 1
      
# Etape 4 : convertir le dictionnaire en une liste de tuples (mot, frequence)

liste_tuples = list(frequence_mots.items())

liste_tuples_triee = sorted(liste_tuples, key=lambda x: x[1], reverse=True)

for mot, frequence in liste_tuples_triee:
  print(f"{mot} : {frequence}")
