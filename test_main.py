import main
import pytest

def test_fun1():
    assert isinstance(main.testFunc1(3.2), int)

def test_func1_2():
    assert main.testFunc1(1) == '1'
