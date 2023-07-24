from lib.lib_errors.present import *
import pytest

def test():
    present = Present()
    
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message2 = str(e.value)

    present.wrap(3)

    with pytest.raises(Exception) as e:
        present.wrap(3)
    error_message1 = str(e.value)
    

    assert error_message1 == "A contents has already been wrapped."
    assert error_message2 == "No contents have been wrapped."