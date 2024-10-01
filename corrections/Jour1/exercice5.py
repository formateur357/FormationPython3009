# Exercice 1

# class Livre:
#     # Attribut de classe pour compter le nombre total de livres créés
#     nombre_de_livres = 0

#     def __init__(self, titre, auteur, pages):
#         """Méthode d'initialisation de la classe Livre."""
#         # Attributs d'instance
#         self.titre = titre
#         self.auteur = auteur
#         self.pages = pages

#         # Incrémentation de l'attribut de classe à chaque création d'instance
#         Livre.nombre_de_livres += 1

#     def __str__(self):
#         """Méthode spéciale pour afficher une représentation informelle du livre."""
#         return f"Titre : {self.titre}, Auteur : {self.auteur}, Pages : {self.pages}"

#     @classmethod
#     def afficher_nombre_de_livres(cls):
#         """Méthode de classe pour afficher le nombre total de livres créés."""
#         print(f"Nombre total de livres : {cls.nombre_de_livres}")


# # Création de plusieurs instances de la classe Livre
# livre1 = Livre("1984", "George Orwell", 328)
# livre2 = Livre("Le Meilleur des mondes", "Aldous Huxley", 288)

# # Affichage des informations des livres
# print(livre1)
# print(livre2)

# # Affichage du nombre total de livres créés
# Livre.afficher_nombre_de_livres()


# ------------------------------------------------------------------------------------------------------------
# Exercice 2

# class CompteBancaire:
#     def __init__(self, solde=0):
#         """Initialise le compte bancaire avec un solde par défaut de 0."""
#         self.solde = solde

#     def deposer(self, montant):
#         """Dépose un montant sur le compte."""
#         if montant > 0:
#             self.solde += montant
#             print(f"Déposé : {montant} €")
#         else:
#             print("Le montant à déposer doit être positif.")

#     def retirer(self, montant):
#         """Retire un montant du compte si le solde est suffisant."""
#         if 0 < montant <= self.solde:
#             self.solde -= montant
#             print(f"Retiré : {montant} €")
#         else:
#             print("Montant invalide ou solde insuffisant.")

#     def __str__(self):
#         """Retourne une représentation en chaîne du compte bancaire."""
#         return f"Solde du compte : {self.solde} €"

#     def __add__(self, autre_compte):
#         """Permet d'ajouter deux comptes bancaires."""
#         # Crée un nouveau compte avec le solde total des deux comptes
#         nouveau_solde = self.solde + autre_compte.solde
#         return CompteBancaire(nouveau_solde)


# # Création de deux comptes bancaires
# compte1 = CompteBancaire(100)
# compte2 = CompteBancaire(200)

# # Opérations de dépôt et de retrait
# compte1.deposer(50)  # Solde compte1 : 150
# compte2.retirer(30)  # Solde compte2 : 170

# # Affichage des soldes des comptes
# print(compte1)
# print(compte2)

# # Addition de deux comptes bancaires
# compte3 = compte1 + compte2

# # Affichage du solde du nouveau compte
# print(compte3)


# ------------------------------------------------------------------------------------------------------------
# Exercice 3

# class Rectangle:
#     def __init__(self, largeur, hauteur):
#         """Initialise le rectangle avec une largeur et une hauteur."""
#         self.__largeur = largeur
#         self.__hauteur = hauteur

#     @property
#     def largeur(self):
#         """Getter pour la largeur."""
#         return self.__largeur

#     @largeur.setter
#     def largeur(self, valeur):
#         """Setter pour la largeur avec vérification."""
#         if valeur > 0:
#             self.__largeur = valeur
#         else:
#             raise ValueError("La largeur doit être positive.")

#     @property
#     def hauteur(self):
#         """Getter pour la hauteur."""
#         return self.__hauteur

#     @hauteur.setter
#     def hauteur(self, valeur):
#         """Setter pour la hauteur avec vérification."""
#         if valeur > 0:
#             self.__hauteur = valeur
#         else:
#             raise ValueError("La hauteur doit être positive.")

#     def __str__(self):
#         """Retourne une représentation en chaîne du rectangle."""
#         return f"Rectangle de largeur {self.__largeur} et hauteur {self.__hauteur}"

#     def __eq__(self, autre):
#         """Compare deux rectangles en fonction de leur aire."""
#         return self.aire() == autre.aire()

#     def aire(self):
#         """Calcule et retourne l'aire du rectangle."""
#         return self.__largeur * self.__hauteur


# # Création de rectangles
# rect1 = Rectangle(10, 5)
# rect2 = Rectangle(5, 10)
# rect3 = Rectangle(3, 7)

# # Affichage des informations du rectangle
# print(rect1)
# print(f"Aire : {rect1.aire()}")

# # Comparaison des rectangles
# print(rect1 == rect2)  # Doit être True (aires égales)
# print(rect1 == rect3)  # Doit être False (aires différentes)


# ------------------------------------------------------------------------------------------------------------
# Exercice 4

# class Cercle:
#     # Attribut de classe pour la valeur de pi
#     pi = 3.14159

#     def __init__(self, rayon):
#         """Initialise le cercle avec un rayon."""
#         self.rayon = rayon

#     def aire(self):
#         """Calcule et retourne l'aire du cercle."""
#         return Cercle.pi * (self.rayon**2)

#     @classmethod
#     def depuis_diametre(cls, diametre):
#         """Méthode de classe pour créer un cercle à partir d'un diamètre."""
#         rayon = diametre / 2
#         return cls(rayon)


# # Création d'un cercle avec le rayon
# cercle1 = Cercle(5)
# print(f"Aire du cercle de rayon 5 : {cercle1.aire()}")

# # Création d'un cercle à partir du diamètre
# cercle2 = Cercle.depuis_diametre(10)
# print(f"Aire du cercle de diamètre 10 : {cercle2.aire()}")


# ------------------------------------------------------------------------------------------------------------
# Exercice 5

class Employe:
    # Attribut de classe pour compter les IDs des employés
    compteur_id = 1

    def __init__(self, prenom, nom, salaire):
        """Initialise un nouvel employé avec un identifiant unique."""
        self.__prenom = prenom
        self.nom = nom
        self.salaire = salaire

        # Attribuer un identifiant unique à l'employé
        self.id = Employe.compteur_id
        Employe.compteur_id += 1

    def __repr__(self):
        """Retourne une représentation officielle de l'employé."""
        return f"Employe(id={self.id}, nom={self.nom}, prenom={self.prenom}, salaire={self.salaire})"

    def __gt__(self, autre):
        """Compare deux employés en fonction de leur salaire."""
        return self.salaire > autre.salaire

    def __lt__(self, autre):
        """Compare deux employés en fonction de leur salaire."""
        return self.salaire < autre.salaire

    def __eq__(self, autre):
        """Vérifie si deux employés ont le même salaire."""
        return self.salaire == autre.salaire


# Création d'employés
emp1 = Employe("Alice", "Dupont", 3000)
emp2 = Employe("Bob", "Martin", 3500)
emp3 = Employe("Charlie", "Durand", 2800)

# Affichage des employés
print(emp1)
print(emp2)

# Comparaison des employés
print(emp1 > emp3)  # True, car 3000 > 2800
print(emp1 > emp2)  # False, car 3000 < 3500
