from lib.lib_functions.report_length import *

def test():
    result = report_length("pee")
    assert result == "This string was 3 characters long."