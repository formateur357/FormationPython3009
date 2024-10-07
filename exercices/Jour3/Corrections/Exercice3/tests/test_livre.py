import pytest

from bibliotheque.livre import Livre


@pytest.fixture
def livre():
    """Fixture pour un livre par défaut."""
    return Livre("1984", "George Orwell")


def test_livre_creation(livre):
    """Test de la création d'un livre."""
    assert livre.titre == "1984"
    assert livre.auteur == "George Orwell"
    assert not livre.emprunte  # Le livre doit être disponible par défaut


def test_livre_preter(livre):
    """Test du prêt d'un livre."""
    livre.preter()
    assert livre.emprunte  # Le livre est maintenant emprunté


def test_livre_retourner(livre):
    """Test du retour d'un livre."""
    livre.preter()
    livre.retourner()
    assert not livre.emprunte  # Le livre est maintenant disponible


def test_livre_deja_empreinte(livre):
    """Test d'une tentative de prêt sur un livre déjà emprunté."""
    livre.preter()
    with pytest.raises(ValueError, match="Le livre '1984' est déjà emprunté."):
        livre.preter()


def test_livre_deja_disponible(livre):
    """Test d'une tentative de retour sur un livre déjà disponible."""
    with pytest.raises(ValueError, match="Le livre '1984' est déjà disponible."):
        livre.retourner()


"""
Bonnes pratiques appliquées :

1. Utilisation des fixtures : Les fixtures sont utilisées pour initialiser les objets récurrents comme les livres, les utilisateurs et la bibliothèque, ce qui permet de réduire la duplication de code et d'améliorer la lisibilité.

2. Test des exceptions avec pytest.raises : Nous utilisons pytest.raises avec un message pour capturer les exceptions attendues de manière plus explicite.

3. Séparation des responsabilités : Chaque test a une responsabilité unique (test de création, test des erreurs, etc.), et les tests sont suffisamment isolés.

4. Utilisation d'assertions explicites : Les assertions sont claires et descriptives.

5. Nettoyage automatique avec tmp_path : Utilisation de tmp_path pour les fichiers temporaires, ce qui permet un nettoyage automatique après chaque test sans avoir besoin de gérer manuellement la suppression des fichiers.
"""
