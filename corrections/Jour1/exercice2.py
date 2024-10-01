"""
Exercice 1 : Filtrage et transformation avec les listes en compréhension

Énoncé
Vous disposez d'une liste de nombres entiers de 1 à 20.
Vous devez créer une nouvelle liste qui contient le carré de chaque nombre pair de la liste initiale.

Solution
"""
# Étape 1 : Créer la liste initiale de 1 à 20
nombres = list(range(1, 21))

# Étape 2 : Utiliser une liste en compréhension pour filtrer les nombres pairs et calculer leur carré

carres_pairs = [n**2 for n in nombres if n % 2 == 0]

# Étape 3 : Afficher la liste résultante
print(carres_pairs)

"""
Exercice 2 : Recherche avec for-else

Énoncé
Vous devez écrire un programme qui vérifie si un nombre donné est un nombre premier.
Si le nombre est premier, affichez un message confirmant qu'il est premier.
Sinon, affichez son plus petit diviseur autre que 1.

Solution
"""
# Étape 1 : Demander à l'utilisateur d'entrer un nombre entier positif supérieur à 1
n = int(input("Entrez un nombre entier positif superieur a 1 : "))

# Vérifier que l'entrée est valide
if n <= 1:
    # Étape 2 : Utiliser une boucle for-else pour vérifier si le nombre est premier
    for i in range(2, n):
        if n% i == 0:
            # Si un diviseur est trouvé, le nombre n'est pas premier
            print(f"{n} n'est pas un nombre premier. Il est divisibke par {i}.")
            break
    else:        
        # Si aucun diviseur n'est trouvé, le nombre est premier
        print(f"{n} est un nombre premier.")

"""
Exercice 3 : Utilisation de l'opérateur ternaire

Énoncé
Écrivez un programme qui demande à l'utilisateur son âge et détermine s'il est majeur ou mineur en utilisant l'opérateur ternaire.

Solution
"""
# Étape 1 : Demander à l'utilisateur d'entrer son âge
age = int(input("Entrez votre age : "))

# Étape 2 : Utiliser l'opérateur ternaire pour déterminer le statut
statut = "majeur" if age >= 18 else "mineur"

# Étape 3 : Afficher le statut
print(f"Vous etes {statut}.")

"""
Exercice 4 : Combinaison des trois concepts

Énoncé
Créez un programme qui génère une liste des 10 premiers nombres entiers positifs.
Pour chaque nombre, si le nombre est divisible par 2, ajoutez son carré à la liste, sinon, ajoutez son cube.
Utilisez une liste en compréhension avec un opérateur ternaire pour cela.
Ensuite, vérifiez si le nombre 100 est présent dans la liste résultante en utilisant une boucle for-else.

Solution
"""
# Étape 1 : Générer la liste des nombres entiers de 1 à 10
nombres = list(range(1, 11))

# Étape 2 : Utiliser une liste en compréhension avec un opérateur ternaire
resultat = [n**2 if n % 2 == 0 else n**3 for n in nombres]

# Étape 3 : Afficher la liste résultante
print(resultat)

# Étape 4 : Utiliser une boucle for-else pour vérifier si 100 est dans la liste
for nombre in resultat:
    if nombre == 100:
        print("100 est dans la liste.")
        break
else:
    print("100 n'est pas dans la liste.")
