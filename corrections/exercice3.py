def puissance(n):
    # La fonction retourne une fonction lambda qui élève x à la puissance n
    return lambda x: x**n


# Création des fonctions carré et cube
carré = puissance(2)
cube = puissance(3)

# Test des fonctions avec le nombre 5
nombre = 5
resultat_carré = carré(nombre)
resultat_cube = cube(nombre)

# Affichage des résultats
print(f"Le carré de {nombre} est {resultat_carré}")
print(f"Le cube de {nombre} est {resultat_cube}")
