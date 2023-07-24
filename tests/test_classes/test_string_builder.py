from lib.lib_classes.string_builder import *

def test():
    build = StringBuilder()
    build1 = build.add("pee")
    size1 = build.size()
    output1 = build.output()
    build2 = build.add("pee")
    size2 = build.size()
    output2 = build.output()
    assert size1 == 3
    assert output1 == "pee"
    assert size2 == 6
    assert output2 == "peepee"