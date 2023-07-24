from lib.lib_classes.counter import *

def test_counter():
    counter = Counter()
    counter.add(6)
    result1 = counter.report()
    assert result1 == "Counted to 6 so far."
    counter.add(6)
    result2 = counter.report()
    assert result2 == "Counted to 12 so far."
    