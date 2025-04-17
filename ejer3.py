def calculadora(a, b, operacion):
    if operacion == "sumar":
        return a + b
    elif operacion == "restar":
        return a - b
    elif operacion == "multiplicar":
        return a * b
    elif operacion == "dividir":
        return a / b
    elif operacion == "potencia":
        return a ** b
    else:
        return "Operación no válida"

# Ejemplo:
print(calculadora(5, 2, "potencia"))
