# Why Type Hints?
# Helps Type Checkers: By hinting at what type you want the object to be the type checker can easily detect if, for instance, you're passing an object with a type that isn't expected.
# Helps with documentation: A third person viewing your code will know what is expected where, ergo, how to use it without getting them TypeErrors.
# Helps IDEs develop more accurate and robust tools:



# 1.) Basic understanding of Type annotations

# def headline(text, align=True):
def headline(text: str, align: bool = True) -> str:
    """ Illustrated the use of type annotation.

    If you define the outcome as str, the interpreter checks whether the thing that is returned is str.
    If not, the PyCharm IDE raises and error by highlighting the part that wil produce the unexpected type.

    Hint: Change str to int, set, bool, float, list, tuple, dict

    """
    if align: # true or not defined
        return f"{text.title()}\n{'-' * len(text)}"
    else: # false
        return f" {text.title()} ".center(50, "o")


print(headline("python type checking"))

print(headline("python type checking", align=False))



# 2.) Issue checking with the help of mypy
# Setup
# run pip install mypy

# Checking for errors:
# in terminal> mypy type_annotation.py
# Success: no issues found in 1 source file


# 3.) a third example
from typing import Dict, List, Tuple

names: List[str] = ["Guido", "Jukka", "Ivan"]
version: Tuple[int, int, int] = (3, 7, 1)
options: Dict[str, bool] = {"centered": False, "capitalize": True}

def my_func(text: List[str]) -> str:
     for x in text:
        print (x)


#my_func(names)


# # 4.) a fourth example
import random
from typing import Sequence, TypeVar
