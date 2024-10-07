x = 10  # Correct
x=10  # Incorrect

appel_fonction(x, y, z) # Correct
appel_fonction( x, y, z ) # Incorrect

# Correct
nombre_utilisateurs = 10
def calculer_moyenne():
  pass 

# Incorrect
NombreUtilisateurs = 10
def CalculerMoyenne():
  pass

# Correct
class UtilisateurActif:
  pass

# Correct
MAX_UTILISATEURS = 100

# Correct
import os # Modules standards
import sys

import numpy as np # Modules tiers

from fibonacci import fibonacci # Correct # Modules locaux
from . import fibonacci # Incorrect

# Incorrect
import os, sys

# Laissez deux lignes vides avant la définition d'une classe ou d'une fonction de niveau supérieur.
# Laissez une ligne vide entre les méthodes d'une classe.


# Correct
def ajouter_element(elements=None):
    if elements is None:
        elements = []
    elements.append(1)
    return elements


# Incorrect
def ajouter_element(elements=[]):
    elements.append(1)
    return elements


# Correct
def ma_fonction(param):
    """
    Cette fonction fait quelque chose avec le paramètre donné.

    :param param: description du paramètre
    :return: description du retour
    """
    pass

# Correct
try:
    fichier = open("fichier.txt", "r")
except FileNotFoundError:
    print("Fichier non trouvé.")

# Incorrect
try:
    fichier = open("fichier.txt", "r")
except Exception:
    print("Erreur.")

# Correct
with open("fichier.txt", "r") as fichier:
    contenu = fichier.read()

# Incorrect
fichier = open("fichier.txt", "r")
contenu = fichier.read()
fichier.close()

# Correct
if mon_liste:  # Si la liste n'est pas vide
    pass

# Incorrect
if len(mon_liste) > 0:
    pass

# Correct
total = (premiere_variable
         + deuxieme_variable
         - troisieme_variable)

# Incorrect
total = premiere_variable + \
        deuxieme_variable - \
        troisieme_variable

# Correct
liste = [1, 2, 3]
dictionnaire = {"clé": "valeur"}

# Incorrect
liste = [ 1, 2, 3 ]
dictionnaire = { "clé" : "valeur" }
