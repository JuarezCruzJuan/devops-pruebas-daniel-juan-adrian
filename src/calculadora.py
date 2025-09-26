def suma(a, b):
    "Función que suma dos números"
    return a + b

def resta(a, b):
    "Función que resta dos números"
    return a - b

def multiplicacion(a, b):
    "Función que multiplica dos números"
    return a * b

def division(a, b):
    "Función que divide dos números"
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b