from lib.test_functions.greet import *

def test_greet():
    result = greet('Harry')
    assert result == "Hello, Harry!"