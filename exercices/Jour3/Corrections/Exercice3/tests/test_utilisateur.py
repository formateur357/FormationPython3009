import pytest

from bibliotheque.livre import Livre
from bibliotheque.utilisateur import Utilisateur


@pytest.fixture
def utilisateur():
    """Fixture pour un utilisateur par défaut."""
    return Utilisateur("Alice")


@pytest.fixture
def livre():
    """Fixture pour un livre par défaut."""
    return Livre("1984", "George Orwell")


def test_utilisateur_creation(utilisateur):
    """Test de la création d'un utilisateur."""
    assert utilisateur.nom == "Alice"
    assert utilisateur.livres_empruntes == []  # Aucune emprunt au départ


def test_utilisateur_emprunter_livre(utilisateur, livre):
    """Test de l'emprunt d'un livre par un utilisateur."""
    utilisateur.emprunter_livre(livre)
    assert livre in utilisateur.livres_empruntes
    assert livre.emprunte  # Le livre doit être marqué comme emprunté


def test_utilisateur_retourner_livre(utilisateur, livre):
    """Test du retour d'un livre par un utilisateur."""
    utilisateur.emprunter_livre(livre)
    utilisateur.retourner_livre(livre)
    assert livre not in utilisateur.livres_empruntes
    assert not livre.emprunte  # Le livre doit être disponible


def test_utilisateur_retourner_livre_non_emprunte(utilisateur, livre):
    """Test de tentative de retour d'un livre non emprunté."""
    with pytest.raises(ValueError, match="n'a pas emprunté le livre"):
        utilisateur.retourner_livre(livre)


"""
Bonnes pratiques appliquées :
1. Utilisation des fixtures : Les fixtures sont utilisées pour initialiser les objets récurrents comme les livres, les utilisateurs et la bibliothèque, ce qui permet de réduire la duplication de code et d'améliorer la lisibilité.

2. Test des exceptions avec pytest.raises : Nous utilisons pytest.raises avec un message pour capturer les exceptions attendues de manière plus explicite.

3. Séparation des responsabilités : Chaque test a une responsabilité unique (test de création, test des erreurs, etc.), et les tests sont suffisamment isolés.

4. Utilisation d'assertions explicites : Les assertions sont claires et descriptives.

5. Nettoyage automatique avec tmp_path : Utilisation de tmp_path pour les fichiers temporaires, ce qui permet un nettoyage automatique après chaque test sans avoir besoin de gérer manuellement la suppression des fichiers.
"""
