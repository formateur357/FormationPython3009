from livre import Livre
from utilisateur import Utilisateur

class Bibliothèque:
    """
    Gère une collection de livres dans une bibliothèque.
    """
    
    def __init__(self):
        """
        Initialise une bibliothèque avec une liste vide de livres.
        """
        self.livres = []  # Collection de livres dans la bibliothèque.
    
    def ajouter_livre(self, livre):
        """
        Ajoute un livre à la bibliothèque.
        
        :param livre: Instance de Livre à ajouter.
        """
        self.livres.append(livre)  # Ajoute le livre à la bibliothèque.
        self.sauvegarder_donnees()  # Sauvegarde l'état après chaque modification.
    
    def supprimer_livre(self, livre):
        """
        Supprime un livre de la bibliothèque.
        
        :param livre: Instance de Livre à supprimer.
        :raises ValueError: Si le livre n'est pas trouvé dans la bibliothèque.
        """
        if livre in self.livres:
            self.livres.remove(livre)  # Supprime le livre s'il est trouvé.
            self.sauvegarder_donnees()  # Sauvegarde après suppression.
        else:
            # Si le livre n'existe pas, une exception est levée.
            raise ValueError(f"Le livre '{livre.titre}' n'existe pas dans la bibliothèque.")
    
    def preter_livre(self, livre, utilisateur):
        """
        Prête un livre à un utilisateur.
        
        :param livre: Instance de Livre à prêter.
        :param utilisateur: Instance de Utilisateur qui emprunte le livre.
        :raises ValueError: Si le livre est indisponible.
        """
        if livre in self.livres and not livre.emprunte:
            utilisateur.emprunter_livre(livre)  # Prête le livre à l'utilisateur.
            self.sauvegarder_donnees()  # Sauvegarde l'état après le prêt.
        else:
            # Si le livre est déjà emprunté, une exception est levée.
            raise ValueError(f"Le livre '{livre.titre}' est indisponible.")
    
    def retourner_livre(self, livre, utilisateur):
        """
        Récupère un livre emprunté par un utilisateur.
        
        :param livre: Instance de Livre à retourner.
        :param utilisateur: Instance de Utilisateur qui retourne le livre.
        """
        utilisateur.retourner_livre(livre)  # Retourne le livre à la bibliothèque.
        self.sauvegarder_donnees()  # Sauvegarde l'état après le retour.
    
    def afficher_rapport(self):
        """
        Affiche un rapport des livres disponibles et empruntés.
        """
        livres_disponibles = [livre for livre in self.livres if not livre.emprunte]
        livres_empruntés = [livre for livre in self.livres if livre.emprunte]

        print("\nLivres disponibles :")
        for livre in livres_disponibles:
            livre.afficher_détails()

        print("\nLivres empruntés :")
        for livre in livres_empruntés:
            livre.afficher_détails()
    
    def sauvegarder_donnees(self):
        """
        Sauvegarde l'état de la bibliothèque dans un fichier texte.
        """
        with open("bibliotheque.txt", "w") as fichier:
            fichier.write("État actuel de la bibliothèque :\n")
            for livre in self.livres:
                etat = "Emprunté" if livre.emprunte else "Disponible"
                fichier.write(f"{livre.titre} - {livre.auteur} - {etat}\n")
