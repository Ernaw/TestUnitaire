
import pytest

def div(first, second):
    assert (second != 0)
    return first / second
def multiple(first, second): #DDdd
    assert(first != 0)
    assert(second != 0)
    return first * second
def add (first, second):
    return first + second

#blabladadaz
def gjgirejngeri():
    option = input("On fait quoi  ? (/,*,+)  \n")
    print(f"My option {option}" )
    option = {
        "+" : print(add(int(input("Nbr: ")), int(input("Nbr2: ")))),
        "*" : print(multiple(int(input("Nbr: ")), int(input("Nbr2: ")))),
        "/" : print(div(int(input("Nbr: ")), int(input("Nbr2: ")))),
    }
    
