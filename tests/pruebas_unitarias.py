import sys
import os
# Agregar el directorio src al path para importar nuestros módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculadora import suma, resta, multiplicacion, division
import pytest

def test_suma():
    "Prueba unitaria para la función suma"
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    "Prueba unitaria para la función resta"
    assert resta(5, 3) == 2
    assert resta(0, 5) == -5
    assert resta(10, 10) == 0

def test_multiplicacion():
    "Prueba unitaria para la función multiplicación"
    assert multiplicacion(3, 4) == 12
    assert multiplicacion(0, 5) == 0
    assert multiplicacion(-2, 3) == -6

def test_division():
    "Prueba unitaria para la función división"
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    assert division(7, 2) == 3.5

def test_division_por_cero():
    "Prueba que la división por cero lance una excepción"
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        division(5, 0)