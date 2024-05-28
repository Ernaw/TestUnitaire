import pytest  
from main import div
from main import add 
from main import multiple 

def call_add(first,second):
    assert(type(first) == int)
    assert(type(second) == int)
    return add(first,second)
def test_add():
    assert  call_add(1,3) == 4


def call_multiple(first,second):
    assert(type(first) == int)
    assert(type(second) == int)
    return multiple(first,second)
def test_multiple():
    assert  call_multiple(2,2) == 4


def call_div(first,second):
    assert(type(first) == int)
    assert(type(second) == int)
    assert(second != 0)
    assert(first != 0)
    return div(first,second)
def test_div():
    assert  call_div(4,2) == 2