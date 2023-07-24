import pytest
from lib.lib_errors.password_checker import * 

def test():
    build = PasswordChecker()
    with pytest.raises(Exception) as e:
        build.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."