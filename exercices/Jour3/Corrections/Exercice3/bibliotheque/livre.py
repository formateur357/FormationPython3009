class Livre:
    """
    Représente un livre avec un titre, un auteur, et un état (disponible ou emprunté).
    """

    def __init__(self, titre, auteur):
        """
        Initialise un nouveau livre avec son titre et son auteur.

        :param titre: Titre du livre.
        :param auteur: Auteur du livre.
        """
        self.titre = titre
        self.auteur = auteur
        self.emprunte = False  # Par défaut, un livre est disponible, donc non emprunté.

    def preter(self):
        """
        Marque le livre comme emprunté.

        :raises ValueError: Si le livre est déjà emprunté.
        """
        if self.emprunte:
            # Si le livre est déjà emprunté, on lève une exception pour signaler cette erreur.
            raise ValueError(f"Le livre '{self.titre}' est déjà emprunté.")
        self.emprunte = True  # Change l'état du livre à emprunté.

    def retourner(self):
        """
        Marque le livre comme retourné (disponible).

        :raises ValueError: Si le livre est déjà disponible.
        """
        if not self.emprunte:
            # Si le livre n'est pas emprunté, lever une exception pour signaler l'erreur.
            raise ValueError(f"Le livre '{self.titre}' est déjà disponible.")
        self.emprunte = False  # Change l'état du livre à disponible.

    def afficher_details(self):
        """
        Affiche les détails du livre (titre, auteur, état).
        """
        etat = "Emprunté" if self.emprunte else "Disponible"
        print(f"Titre: {self.titre}, Auteur: {self.auteur}, État: {etat}")
