import pytest

from calcul import addition, division

def test_addition():
  assert addition(2, 3) == 5
  assert addition(-1, 1) == 0
  assert addition(0, 0) == 0
  
def test_division_par_zero():
  with pytest.raises(ZeroDivisionError):
    division(10, 0)