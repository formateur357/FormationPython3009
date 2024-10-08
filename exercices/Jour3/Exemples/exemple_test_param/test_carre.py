import pytest

from .carre import carre

@pytest.mark.parametrize("n, attendu", [
  (2, 4),
  (-3, 9),
  (0, 0),
  (1.5, 2.25)
])
def test_carre_parametres(n, attendu):
  assert carre(n) == attendu