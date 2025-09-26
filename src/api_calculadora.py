from flask import Flask, request, jsonify
from calculadora import suma, resta, multiplicacion, division

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    "Endpoint para verificar que la API está funcionando"
    return jsonify({
        "status": "OK",
        "message": "API Calculadora funcionando correctamente"
    })

@app.route('/suma', methods=['POST'])
def api_suma():
    "Endpoint para sumar dos números"
    try:
        data = request.get_json()
        a = data['a']
        b = data['b']
        resultado = suma(a, b)
        return jsonify({
            "operacion": "suma",
            "a": a,
            "b": b,
            "resultado": resultado
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/resta', methods=['POST'])
def api_resta():
    "Endpoint para restar dos números"
    try:
        data = request.get_json()
        a = data['a']
        b = data['b']
        resultado = resta(a, b)
        return jsonify({
            "operacion": "resta",
            "a": a,
            "b": b,
            "resultado": resultado
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/multiplicacion', methods=['POST'])
def api_multiplicacion():
    "Endpoint para multiplicar dos números"
    try:
        data = request.get_json()
        a = data['a']
        b = data['b']
        resultado = multiplicacion(a, b)
        return jsonify({
            "operacion": "multiplicacion",
            "a": a,
            "b": b,
            "resultado": resultado
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/division', methods=['POST'])
def api_division():
    "Endpoint para dividir dos números"
    try:
        data = request.get_json()
        a = data['a']
        b = data['b']
        resultado = division(a, b)
        return jsonify({
            "operacion": "division",
            "a": a,
            "b": b,
            "resultado": resultado
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/operacion-compleja', methods=['POST'])
def api_operacion_compleja():
    "Endpoint para operación compleja: (a + b) * c"
    try:
        data = request.get_json()
        a = data['a']
        b = data['b']
        c = data['c']
        
        # (a + b) * c
        suma_resultado = suma(a, b)
        resultado_final = multiplicacion(suma_resultado, c)
        
        return jsonify({
            "operacion": "operacion_compleja",
            "formula": "(a + b) * c",
            "a": a,
            "b": b,
            "c": c,
            "resultado": resultado_final
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)