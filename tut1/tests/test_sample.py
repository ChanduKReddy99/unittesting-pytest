"""sample unitesting using pytest module in python"""

from tut1.main.sample import add
def test_add():
    """ this method adds 2 variables"""
    assert add(3,4)==7
def test_add_str():
    """this method adding 2 string varibales"""
    assert add("python-", "pytest")== "python-pytest"

#combining the above 2 methods using python class
class Testsample():
    """this class combines both the above methods"""
    def test_add(self):
        """this method tests adding 2 variables"""
        assert add(3,4)==7
    def test_add_str(self):
        """this method tests the adding of 2 string variables"""
        assert add("python-", "pytest")== "python-pytest"
        