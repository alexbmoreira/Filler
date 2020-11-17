if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "tests"
    
from ..core.models import Color

def test_color():
    color = Color("red")
    assert color.name == "red"