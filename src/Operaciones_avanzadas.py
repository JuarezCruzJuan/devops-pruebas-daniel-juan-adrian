from calculadora import suma, resta, multiplicacion, division

class CalculadoraAvanzada:
    "Clase que integra múltiples operaciones de la calculadora básica"
    
    def __init__(self):
        self.historial = []
    
    def operacion_compleja(self, a, b, c):
        "Realiza una operación compleja: (a + b) * c"
        resultado_suma = suma(a, b)
        resultado_final = multiplicacion(resultado_suma, c)
        
        operacion = f"({a} + {b}) * {c} = {resultado_final}"
        self.historial.append(operacion)
        
        return resultado_final
    
    def promedio_de_division(self, numeros, divisor):
        "Calcula el promedio de una lista de números y lo divide por un divisor"
        if not numeros:
            raise ValueError("La lista no puede estar vacía")
        
        # Sumar todos los números usando nuestra función suma
        total = numeros[0]
        for numero in numeros[1:]:
            total = suma(total, numero)
        
        # Calcular promedio
        promedio = division(total, len(numeros))
        
        # Dividir el promedio por el divisor
        resultado = division(promedio, divisor)
        
        operacion = f"Promedio de {numeros} dividido por {divisor} = {resultado}"
        self.historial.append(operacion)
        
        return resultado
    
    def ecuacion_cuadratica_simple(self, a, b, c, x):
        "Evalúa ax² + bx + c usando nuestras funciones básicas"
        # Calcular x²
        x_cuadrado = multiplicacion(x, x)
        
        # Calcular ax²
        ax_cuadrado = multiplicacion(a, x_cuadrado)
        
        # Calcular bx
        bx = multiplicacion(b, x)
        
        # Calcular ax² + bx
        suma_parcial = suma(ax_cuadrado, bx)
        
        # Calcular resultado final: ax² + bx + c
        resultado = suma(suma_parcial, c)
        
        operacion = f"{a}*{x}² + {b}*{x} + {c} = {resultado}"
        self.historial.append(operacion)
        
        return resultado
    
    def obtener_historial(self):
        "Retorna el historial de operaciones"
        return self.historial.copy()
    
    def limpiar_historial(self):
        "Limpia el historial de operaciones"
        self.historial.clear()