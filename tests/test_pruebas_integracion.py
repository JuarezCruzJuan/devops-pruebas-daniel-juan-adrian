import sys
import os
# Agregar el directorio src al path para importar nuestros módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculadora import suma, resta, multiplicacion, division
from Operaciones_avanzadas import CalculadoraAvanzada
import pytest

def test_operacion_compleja():
    "Prueba que suma y multiplicación trabajen juntas"
    calc = CalculadoraAvanzada()
    resultado = calc.operacion_compleja(2, 3, 4)  # (2+3)*4 = 20
    assert resultado == 20

def test_promedio_division():
    "Prueba que suma y división trabajen juntas para calcular promedio"
    calc = CalculadoraAvanzada()
    numeros = [10, 20, 30]  # Promedio = 20, dividido por 2 = 10
    resultado = calc.promedio_de_division(numeros, 2)
    assert resultado == 10.0

def test_ecuacion_simple():
    "Prueba múltiples operaciones en una ecuación simple"
    calc = CalculadoraAvanzada()
    # 2*1² + 3*1 + 1 = 2 + 3 + 1 = 6
    resultado = calc.ecuacion_cuadratica_simple(2, 3, 1, 1)
    assert resultado == 6

def test_historial_funciona():
    "Prueba que el historial guarde las operaciones"
    calc = CalculadoraAvanzada()
    calc.operacion_compleja(1, 1, 2)  # (1+1)*2 = 4
    historial = calc.obtener_historial()
    assert len(historial) == 1
    assert "4" in historial[0]

def test_division_por_cero_en_promedio():
    "Prueba que el error se propague correctamente"
    calc = CalculadoraAvanzada()
    with pytest.raises(ValueError):
        calc.promedio_de_division([1, 2, 3], 0)

def test_flujo_basico():
    "Prueba un flujo simple usando varias operaciones"
    # Usar directamente las funciones básicas juntas
    a = suma(5, 3)      # 8
    b = resta(a, 2)     # 6
    c = multiplicacion(b, 2)  # 12
    d = division(c, 4)  # 3
    
    assert d == 3.0