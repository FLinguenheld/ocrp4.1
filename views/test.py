
from typing import (Callable)


DEBUG: bool = False
# DEBUG: bool = True


def log(debug: bool=True):

    def decorator(function: Callable):

        def wrapper(*args, **kwargs):
            if debug:
                print(function.__name__)

            return function(*args, **kwargs)

        return wrapper 

    return decorator



@log(debug=DEBUG)
def toto():
    print("la tete à toto")

@log(debug=DEBUG)
def tata(x: int):
    print(x ** 2)

@log(debug=DEBUG)
def tutu(x: int):
    return x ** 3




# log(toto)()
# log(tata)()
# tata(x=5)
print(tutu(x=5))

toto()
tata(10)
