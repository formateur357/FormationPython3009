import pytest

from bibliotheque.gestionnaire_fichier import sauvegarder_donnees, charger_donnees
from bibliotheque.livre import Livre
from bibliotheque.bibliotheque import Bibliothèque


@pytest.fixture
def bibliotheque():
    """Fixture qui crée une bibliothèque avec quelques livres."""
    bibliotheque = Bibliothèque()
    livre1 = Livre("1984", "George Orwell")
    livre2 = Livre("Le Meilleur des Mondes", "Aldous Huxley")
    bibliotheque.ajouter_livre(livre1)
    bibliotheque.ajouter_livre(livre2)
    return bibliotheque


def test_sauvegarder_donnees(bibliotheque, tmp_path):
    """Test de la sauvegarde des données dans un fichier."""
    fichier_test = tmp_path / "bibliotheque.txt"
    sauvegarder_donnees(bibliotheque, fichier_test)
    assert fichier_test.exists()


def test_charger_donnees(bibliotheque, tmp_path):
    """Test du chargement des données depuis un fichier."""
    fichier_test = tmp_path / "bibliotheque.txt"
    sauvegarder_donnees(bibliotheque, fichier_test)
    nouvelle_bibliotheque = charger_donnees(fichier_test)
    assert len(nouvelle_bibliotheque.livres) == 2
    assert nouvelle_bibliotheque.livres[0].titre == "1984"


"""
Bonnes pratiques appliquées :
1. Utilisation des fixtures : Les fixtures sont utilisées pour initialiser les objets récurrents comme les livres, les utilisateurs et la bibliothèque, ce qui permet de réduire la duplication de code et d'améliorer la lisibilité.

2. Test des exceptions avec pytest.raises : Nous utilisons pytest.raises avec un message pour capturer les exceptions attendues de manière plus explicite.

3. Séparation des responsabilités : Chaque test a une responsabilité unique (test de création, test des erreurs, etc.), et les tests sont suffisamment isolés.

4. Utilisation d'assertions explicites : Les assertions sont claires et descriptives.

5. Nettoyage automatique avec tmp_path : Utilisation de tmp_path pour les fichiers temporaires, ce qui permet un nettoyage automatique après chaque test sans avoir besoin de gérer manuellement la suppression des fichiers.
"""
