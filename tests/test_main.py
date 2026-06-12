from src.main import add
import pytest

def test_ad():
  assert add(2,3) == 5
  assert add(1,2, 3.5) == 4.7
