# PROBLEMA
# Calcular el importe a pagar por un viaje en taxi basado en el banderazo, los kilómetros recorridos y un descuento por distancia.
# ENTRADAS
# kilometros: float, km, mayor a 0.
# SALIDAS
# importe: float, pesos, formato con dos decimales, mostrado en tabla usando tabulate.
# REGLAS Y SUPUESTOS
# Cobro de banderazo fijo: $35.00.
# Tarifa por kilómetro: $9.00 por km.
# Si los viajes son de más de 20 km (kilometros > 20), se aplica un 10% de descuento sobre el costo total calculado.
# ALGORITMO
# 1. Leer los kilómetros.
# 2. Calcular subtotal = 35.0 + (kilometros * 9.0)
# 3. Si kilometros > 20:
#      importe = subtotal * 0.90
# 4. En caso contrario:
#      importe = subtotal
# 5. Mostrar el importe usando tabulate.
# CASOS DE PRUEBA
# 5 -> 80.00
# 20 -> 215.00
# 21 -> 212.40
# 30 -> 293.40
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# La única biblioteca permitida es tabulate. No importes ningún otro módulo.
# No agregues clases, funciones auxiliares adicionales.
# No agregues validaciones, mensajes extra que no estén aquí.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerKilometros() -> float
# calcularImporte(kilometros: float) -> float
# mostrarImporte(kilometros: float, importe: float) -> None

from tabulate import tabulate

def leerKilometros():
    return float(input("Ingrese los kilómetros recorridos: "))

def calcularImporte(kilometros):
    subtotal = 35.0 + (kilometros * 9.0)
    if kilometros > 20:
        importe = subtotal * 0.90
    else:
        importe = subtotal
    return importe

def mostrarImporte(kilometros, importe):
    filas = [
        ["Kilómetros recorridos", kilometros],
        ["Importe total", f"${importe:.2f}"]
    ]
    print(tabulate(filas, headers=["Concepto", "Valor"]))