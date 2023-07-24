from lib.lib_classes.gratitudes import *

def test():
    build = Gratitudes()
    build.add("Python")
    output1 = build.format()
    build.add("I Prevail")
    output2 = build.format()
    assert output1 == "Be grateful for: Python"
    assert output2 == "Be grateful for: Python, I Prevail"