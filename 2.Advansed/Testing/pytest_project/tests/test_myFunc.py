import pytest
from ..myFunc.main import *


def test_main():
    assert main() == "ok", "ERROR not OK"


@pytest.mark.skip  # Пропустить тест
def test_func1():
    assert func1() == "ok", "ERROR not OK"


def test_summ():
    a = 1
    b = 2
    assert summ(a, b) == a + b, "ERROR"
