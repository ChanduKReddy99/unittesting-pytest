""" writing pytest with exception handling """
import pytest
from tut1.main.sample2 import valid_age


def test_valid_age():
    """this method validates the age """
    valid_age(20)
def test_invalid_age():
    """this method invalidates the age"""
    with pytest.raises(ValueError) as excinfo:
        valid_age(-1)
    assert "age can't be less than zero" in str(excinfo.value)
        
