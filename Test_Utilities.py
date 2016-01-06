import pytest
from Utilities import relative_average

def test_relative_average():
    assert relative_average([1, 2, 3], 1) == 2
    assert relative_average([1, 2, 3], 2) == 1