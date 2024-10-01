#############################################################################
# Exercice 1


def diviser(a, b):
    """
    Fonction qui divise 'a' par 'b' et affiche le résultat.
    Gère les exceptions potentielles, notamment la division par zéro.

    :param a: Le numérateur.
    :param b: Le dénominateur.
    """
    try:
        # Tentative de division
        resultat = a / b
    except ZeroDivisionError:
        # Gestion de l'exception si b est égal à zéro
        print("Erreur : Division par zéro.")
    else:
        # Ce bloc s'exécute si aucune exception n'est levée dans le bloc try
        print(f"Le résultat est : {resultat}")
        print("Opération réussie.")
    finally:
        # Ce bloc s'exécute dans tous les cas, qu'il y ait une exception ou non
        print("Opération terminée.")


# Cas de test
diviser(10, 2)  # Cas où la division réussit
print()  # Ligne vide pour la lisibilité
diviser(5, 0)  # Cas où une division par zéro se produit

"""
Points clés à retenir :

Gestion des exceptions avec try-except :

. Le bloc try contient le code qui peut potentiellement lever une exception.
. Le bloc except capture l'exception spécifique et permet de gérer l'erreur sans interrompre le programme.

Bloc else :

. S'exécute uniquement si aucune exception n'est levée dans le bloc try.
. Utile pour le code qui doit s'exécuter lorsque tout se passe bien.

Bloc finally :

. S'exécute dans tous les cas, qu'il y ait une exception ou non.
. Utile pour le nettoyage des ressources ou pour signaler la fin d'une opération.
"""
#############################################################################
# Exercice 2

import math


class ValeurNegativeError(Exception):
    """
    Exception personnalisée levée lorsque la valeur est négative.
    """

    def __init__(self, message="La valeur ne peut pas être négative."):
        """
        Initialise l'exception avec un message d'erreur.

        :param message: Le message d'erreur à afficher.
        """
        super().__init__(message)


def racine_carree(n):
    """
    Calcule la racine carrée de 'n' si 'n' est positif.
    Lève une exception ValeurNegativeError si 'n' est négatif.

    :param n: Le nombre dont on veut calculer la racine carrée.
    :return: La racine carrée de 'n'.
    :raises ValeurNegativeError: Si 'n' est négatif.
    """
    if n < 0:
        # Lève l'exception personnalisée avec un message spécifique
        raise ValeurNegativeError(
            f"Impossible de calculer la racine carrée d'un nombre négatif ({n})."
        )
    else:
        # Retourne la racine carrée de 'n'
        return math.sqrt(n)


# Cas de test
try:
    print(racine_carree(9))  # Cas où 'n' est positif
    print(racine_carree(-5))  # Cas où 'n' est négatif
except ValeurNegativeError as e:
    # Capture et affiche le message de l'exception personnalisée
    print(e)

"""
Points clés à retenir :

Création d'une exception personnalisée :

. Créez une classe qui hérite de Exception ou de l'une de ses sous-classes.
. Personnalisez le constructeur pour accepter des messages ou des données supplémentaires.

Levée d'une exception avec raise:

. Utilisez l'instruction raise pour lever une exception.
. Fournissez une instance de l'exception avec un message détaillé si nécessaire.

Gestion des exceptions personnalisées :

. Utilisez un bloc try-except pour capturer et gérer l'exception spécifique.
"""

#############################################################################
# Exercice 3


def lire_entier():
    """
    Demande à l'utilisateur d'entrer un nombre entier.
    Gère les exceptions ValueError et KeyboardInterrupt.

    :return: Le nombre entier saisi par l'utilisateur.
    """
    try:
        # Demande de saisie à l'utilisateur
        nombre = int(input("Entrez un nombre entier : "))
        print(f"Vous avez entré : {nombre}")
    except ValueError:
        # Gestion de l'exception si la conversion en entier échoue
        print("Erreur : Veuillez entrer un nombre entier valide.")
    except KeyboardInterrupt:
        # Gestion de l'exception si l'utilisateur interrompt le programme
        print("\nOpération annulée par l'utilisateur.")
    else:
        # Ce bloc s'exécute si aucune exception n'est levée
        print("Merci pour votre saisie.")
    finally:
        # Ce bloc s'exécute dans tous les cas
        print("Fin de la fonction.")


# Appel de la fonction
lire_entier()

"""
Points clés à retenir :

Gestion de plusieurs exceptions :

. Utilisez plusieurs blocs except pour capturer et gérer différents types d'exceptions.
. Placez les exceptions les plus spécifiques avant les plus générales.

Exceptions courantes :

. ValueError : Se produit lorsque la conversion d'un type de données échoue.
. KeyboardInterrupt : Se produit lorsque l'utilisateur interrompt le programme avec une interruption du clavier.

Bloc else avec try-except:

. Le bloc else est utile pour exécuter du code uniquement si aucune exception n'est levée dans le bloc try.

Bloc finally:

. Utile pour exécuter du code de nettoyage ou pour indiquer la fin d'une opération.
"""
