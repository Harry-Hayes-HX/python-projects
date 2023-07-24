from lib.lib_functions.check_codeword import *

def test():
    result1 = check_codeword("horse")
    assert result1 == "Correct! Come in."
    result2 = check_codeword("house")
    assert result2 == "Close, but nope."
    result3 = check_codeword("eeeee")
    assert result3 == "WRONG!"
