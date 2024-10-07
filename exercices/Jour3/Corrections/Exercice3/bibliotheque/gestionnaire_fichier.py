# gestionnaire_fichier.py
from .bibliotheque import Bibliothèque
from .livre import Livre


def sauvegarder_donnees(bibliotheque, nom_fichier="bibliotheque.txt"):
    """
    Sauvegarde l'état de la bibliothèque dans un fichier texte.

    :param bibliotheque: Instance de Bibliothèque dont l'état doit être sauvegardé.
    :param nom_fichier: Nom du fichier où sauvegarder les données.
    """
    with open(nom_fichier, "w") as fichier:
        fichier.write("État actuel de la bibliothèque :\n")
        for livre in bibliotheque.livres:
            etat = "Emprunté" if livre.emprunte else "Disponible"
            fichier.write(f"{livre.titre} - {livre.auteur} - {etat}\n")


def charger_donnees(nom_fichier="bibliotheque.txt"):
    """
    Charge l'état de la bibliothèque depuis un fichier texte.

    :param nom_fichier: Nom du fichier d'où charger les données.
    :return: Une instance de Bibliothèque.
    """
    bibliotheque = Bibliothèque()
    try:
        with open(nom_fichier, "r") as fichier:
            for ligne in fichier.readlines()[
                1:
            ]:  # Ignorer la première ligne de l'en-tête
                titre, auteur, etat = ligne.strip().split(" - ")
                livre = Livre(titre, auteur)
                if etat == "Emprunté":
                    livre.emprunte = True
                bibliotheque.ajouter_livre(livre)
    except FileNotFoundError:
        print(
            f"Le fichier '{nom_fichier}' n'existe pas. Une nouvelle bibliothèque sera créée."
        )
    return bibliotheque
