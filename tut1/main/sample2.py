"""how to write exception in pytest to pass the test """

def valid_age(age):
    """this method gives the a valid age of a person """
    if age < 0:
        raise ValueError(" age can't be less than zero")
