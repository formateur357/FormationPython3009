#######################################################################################
# Exercice 1

# Définition de la classe de base Vehicule
class Vehicule:
    """
    Classe de base représentant un véhicule générique.
    """

    def __init__(self, marque, modele):
        """
        Constructeur qui initialise les attributs marque et modèle.

        :param marque: La marque du véhicule.
        :param modele: Le modèle du véhicule.
        """
        self.marque = marque
        self.modele = modele

    def demarrer(self):
        """
        Méthode qui affiche un message indiquant que le véhicule démarre.
        """
        print(f"Le véhicule {self.marque} {self.modele} démarre.")


# Définition de la classe dérivée Voiture qui hérite de Vehicule
class Voiture(Vehicule):
    """
    Classe représentant une voiture, dérivée de Vehicule.
    """

    def __init__(self, marque, modele, nombre_de_portes):
        """
        Constructeur qui initialise les attributs de Vehicule et ajoute nombre_de_portes.

        :param marque: La marque de la voiture.
        :param modele: Le modèle de la voiture.
        :param nombre_de_portes: Le nombre de portes de la voiture.
        """
        super().__init__(marque, modele)  # Appel du constructeur de la classe de base
        self.nombre_de_portes = nombre_de_portes

    def demarrer(self):
        """
        Surcharge de la méthode demarrer() pour afficher un message spécifique à la voiture.
        """
        print(f"La voiture {self.marque} {self.modele} démarre.")

    def afficher_info(self):
        """
        Méthode qui affiche les informations de la voiture.
        """
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Nombre de portes : {self.nombre_de_portes}")


# Création d'une instance de Voiture
ma_voiture = Voiture("Toyota", "Corolla", 4)

# Appel de la méthode demarrer()
ma_voiture.demarrer()

# Appel de la méthode afficher_info()
ma_voiture.afficher_info()

"""
Points clés à retenir :

Héritage simple :
La classe dérivée hérite des attributs et méthodes de la classe de base.
super().__init__() est utilisé pour appeler le constructeur de la classe de base.
Les méthodes de la classe de base peuvent être surchargées dans la classe dérivée.
"""

#######################################################################################
# Exercice 2


# Définition de la classe Mangeur
class Mangeur:
    """
    Classe représentant un mangeur.
    """

    def manger(self):
        """
        Méthode qui affiche un message indiquant que l'entité mange de la nourriture.
        """
        print("Mange de la nourriture.")


# Définition de la classe Dormeur
class Dormeur:
    """
    Classe représentant un dormeur.
    """

    def dormir(self):
        """
        Méthode qui affiche un message indiquant que l'entité dort paisiblement.
        """
        print("Dort paisiblement.")

    def manger(self):
        """
        Méthode qui affiche un message indiquant que l'entité mange avant de dormir.
        """
        print("Mange avant de dormir.")


# Définition de la classe Animal qui hérite de Mangeur et Dormeur
class Animal(Mangeur, Dormeur):
    """
    Classe représentant un animal, qui hérite de Mangeur et Dormeur.
    """

    pass  # Aucune méthode supplémentaire n'est nécessaire


# Création d'une instance de Animal
mon_animal = Animal()

# Appel des méthodes manger() et dormir()
mon_animal.manger()
mon_animal.dormir()

# Afficher l'ordre de résolution des méthodes (MRO)
print(Animal.__mro__)

"""
Analyse du résultat :

. Pourquoi la méthode manger() de Mangeur est-elle appelée ?
  . Parce que Mangeur apparaît avant Dormeur dans le MRO.
  . Python utilise le premier manger() qu'il trouve en suivant le MRO.

Points clés à retenir :

. Héritage multiple :
  . Une classe peut hériter de plusieurs classes.
  . L'ordre des classes parentes dans la définition influence le MRO.

. Ordre de résolution des méthodes (MRO) :
  . Détermine l'ordre dans lequel Python recherche les méthodes.
  . Peut être consulté avec Classe.__mro__.
"""

#######################################################################################
# Exercice 3


# Définition de la classe de base A
class A:
    def afficher(self):
        print("Classe A")


# Définition de la classe B qui hérite de A
class B(A):
    def afficher(self):
        print("Classe B")


# Définition de la classe C qui hérite de A
class C(A):
    def afficher(self):
        print("Classe C")


# Définition de la classe D qui hérite de B et C
class D(B, C):
    pass  # Aucune méthode supplémentaire n'est nécessaire


# Création d'une instance de D
d = D()

# Appel de la méthode afficher()
d.afficher()

# Afficher l'ordre de résolution des méthodes (MRO)
print(D.__mro__)

"""
Analyse du résultat :

. Pourquoi la méthode afficher() de la classe B est-elle appelée ?

  . Python suit l'ordre de résolution des méthodes (MRO).
  . Dans D.__mro__, après D, la première classe est B.
  . La méthode afficher() est trouvée dans B, donc elle est appelée avant de chercher dans C ou A.

. Comment Python résout-il le problème du diamant ?

  . Le problème du diamant se produit lorsque plusieurs classes héritent d'une même classe de base et qu'une classe dérivée hérite de ces classes.
  . Python utilise le MRO pour résoudre ce problème.
  . Le MRO est calculé en utilisant l'algorithme C3, qui assure une résolution cohérente et évite les ambiguïtés.
"""
