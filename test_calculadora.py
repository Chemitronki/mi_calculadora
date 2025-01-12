import pytest
from Calculadora import Calculadora

def test_sumar():
    calc = Calculadora()
    assert calc.sumar(3, 5) == 8
    assert calc.sumar(-1, 1) == 0
    assert calc.sumar(0, 0) == 0

def test_restar():
    calc = Calculadora()
    assert calc.restar(10, 5) == 5
    assert calc.restar(0, 5) == -5
    assert calc.restar(5, 0) == 5

def test_multiplicar():
    calc = Calculadora()
    assert calc.multiplicar(3, 5) == 15
    assert calc.multiplicar(-3, -5) == 15
    assert calc.multiplicar(3, 0) == 0

def test_dividir():
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5
    assert calc.dividir(-10, -2) == 5
    with pytest.raises(ValueError):
        calc.dividir(10, 0)
