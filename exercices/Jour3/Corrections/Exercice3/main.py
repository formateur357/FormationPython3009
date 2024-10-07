# main.py
from bibliotheque.bibliotheque import Bibliothèque
from bibliotheque.livre import Livre
from bibliotheque.utilisateur import Utilisateur
from bibliotheque.gestionnaire_fichier import sauvegarder_donnees, charger_donnees


def main():
    """
    Point d'entrée principal du programme.
    Permet à l'utilisateur d'interagir avec la bibliothèque.
    """
    # Charger la bibliothèque existante ou en créer une nouvelle
    bibliotheque = charger_donnees()

    # Simuler des interactions utilisateur
    utilisateur = Utilisateur("Alice")

    # Ajouter un livre et prêter un livre
    livre1 = Livre("1984", "George Orwell")
    bibliotheque.ajouter_livre(livre1)
    bibliotheque.preter_livre(livre1, utilisateur)

    # Afficher le rapport
    bibliotheque.afficher_rapport()

    # Retourner un livre et afficher le rapport
    bibliotheque.retourner_livre(livre1, utilisateur)
    bibliotheque.afficher_rapport()

    # Sauvegarder les modifications
    sauvegarder_donnees(bibliotheque)


if __name__ == "__main__":
    main()
