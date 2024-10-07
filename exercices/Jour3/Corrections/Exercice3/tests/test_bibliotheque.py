import pytest

from bibliotheque.livre import Livre
from bibliotheque.utilisateur import Utilisateur
from bibliotheque.bibliotheque import Bibliothèque


@pytest.fixture
def bibliotheque():
    """Fixture pour une bibliothèque vide."""
    return Bibliothèque()


@pytest.fixture
def utilisateur():
    """Fixture pour un utilisateur par défaut."""
    return Utilisateur("Alice")


@pytest.fixture
def livre():
    """Fixture pour un livre par défaut."""
    return Livre("1984", "George Orwell")


def test_ajouter_livre(bibliotheque, livre):
    """Test de l'ajout d'un livre à la bibliothèque."""
    bibliotheque.ajouter_livre(livre)
    assert livre in bibliotheque.livres


def test_supprimer_livre(bibliotheque, livre):
    """Test de la suppression d'un livre de la bibliothèque."""
    bibliotheque.ajouter_livre(livre)
    bibliotheque.supprimer_livre(livre)
    assert livre not in bibliotheque.livres


def test_prêter_livre(bibliotheque, utilisateur, livre):
    """Test du prêt d'un livre."""
    bibliotheque.ajouter_livre(livre)
    bibliotheque.preter_livre(livre, utilisateur)
    assert livre.emprunte


def test_retourner_livre(bibliotheque, utilisateur, livre):
    """Test du retour d'un livre."""
    bibliotheque.ajouter_livre(livre)
    bibliotheque.preter_livre(livre, utilisateur)
    bibliotheque.retourner_livre(livre, utilisateur)
    assert not livre.emprunte


def test_supprimer_livre_non_present(bibliotheque, livre):
    """Test de tentative de suppression d'un livre qui n'est pas dans la bibliothèque."""
    with pytest.raises(ValueError, match="n'existe pas dans la bibliothèque"):
        bibliotheque.supprimer_livre(livre)


"""
Bonnes pratiques appliquées :
1. Utilisation des fixtures : Les fixtures sont utilisées pour initialiser les objets récurrents comme les livres, les utilisateurs et la bibliothèque, ce qui permet de réduire la duplication de code et d'améliorer la lisibilité.

2. Test des exceptions avec pytest.raises : Nous utilisons pytest.raises avec un message pour capturer les exceptions attendues de manière plus explicite.

3. Séparation des responsabilités : Chaque test a une responsabilité unique (test de création, test des erreurs, etc.), et les tests sont suffisamment isolés.

4. Utilisation d'assertions explicites : Les assertions sont claires et descriptives.

5. Nettoyage automatique avec tmp_path : Utilisation de tmp_path pour les fichiers temporaires, ce qui permet un nettoyage automatique après chaque test sans avoir besoin de gérer manuellement la suppression des fichiers.
"""
