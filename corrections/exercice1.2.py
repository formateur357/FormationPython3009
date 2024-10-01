class CompteurPersonnalisé:
    """
    Une classe itérable personnalisée qui compte de 'debut' jusqu'à 'fin' (non inclus).
    """

    def __init__(self, debut, fin):
        """
        Initialise le compteur avec les valeurs de début et de fin.

        :param debut: La valeur à partir de laquelle le compteur commence.
        :param fin: La valeur à laquelle le compteur se termine (non inclus).
        """
        self.debut = debut  # Stocke la valeur de départ
        self.fin = fin  # Stocke la valeur de fin
        self.courant = debut  # Initialise la valeur courante du compteur

    def __iter__(self):
        """
        Rendre l'objet itérable en retournant l'itérateur.

        :return: Retourne l'objet itérateur (ici, l'objet lui-même).
        """
        return self  # Retourne self car __next__ est défini dans la classe

    def __next__(self):
        """
        Retourne la prochaine valeur dans la séquence.

        :return: La valeur suivante du compteur.
        :raises StopIteration: Lorsque la valeur courante atteint ou dépasse 'fin'.
        """
        if self.courant < self.fin:
            valeur = self.courant  # Sauvegarde la valeur actuelle
            self.courant += (
                1  # Incrémente la valeur courante pour la prochaine itération
            )
            return valeur  # Retourne la valeur actuelle
        else:
            raise StopIteration  # Lève StopIteration pour arrêter l'itération


# Exemple d'utilisation de la classe CompteurPersonnalisé
if __name__ == "__main__":
    compteur = CompteurPersonnalisé(1, 5)  # Crée une instance avec debut=1 et fin=5
    for nombre in compteur:  # Itère sur l'objet compteur
        print(nombre)  # Affiche chaque nombre
