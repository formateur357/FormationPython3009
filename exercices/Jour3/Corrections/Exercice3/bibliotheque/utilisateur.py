class Utilisateur:
    """
    Représente un utilisateur de la bibliothèque avec une liste de livres empruntés.
    """

    def __init__(self, nom):
        """
        Initialise un utilisateur avec son nom et une liste de livres empruntés.

        :param nom: Nom de l'utilisateur.
        """
        self.nom = nom
        self.livres_empruntes = []  # L'utilisateur commence avec zéro livre emprunté.

    def emprunter_livre(self, livre):
        """
        Ajoute un livre à la liste des livres empruntés de l'utilisateur et marque le livre comme emprunté.

        :param livre: Instance de Livre à emprunter.
        """
        self.livres_empruntes.append(
            livre
        )  # Ajoute le livre à la liste de l'utilisateur.
        livre.preter()  # Marque le livre comme emprunté.

    def retourner_livre(self, livre):
        """
        Retire un livre de la liste des livres empruntés de l'utilisateur et marque le livre comme retourné.

        :param livre: Instance de Livre à retourner.
        :raises ValueError: Si l'utilisateur n'a pas emprunté ce livre.
        """
        if livre in self.livres_empruntes:
            self.livres_empruntes.remove(
                livre
            )  # Retire le livre de la liste des livres empruntés.
            livre.retourner()  # Marque le livre comme disponible.
        else:
            # Si l'utilisateur tente de retourner un livre qu'il n'a pas emprunté, une exception est levée.
            raise ValueError(f"{self.nom} n'a pas emprunté le livre '{livre.titre}'.")
