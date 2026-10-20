# PROBLEMA
# Calcular la multa por retraso en la devolución de un libro de biblioteca de acuerdo con los días de retraso y un tope máximo.
# ENTRADAS
# dias: int, días de retraso, mayor o igual a 0.
# SALIDAS
# multa: float, pesos, formato con dos decimales, mostrado en tabla usando tabulate.
# REGLAS Y SUPUESTOS
# $5 por cada día de retraso durante los primeros 10 días (dias <= 10).
# A partir del día 11 de retraso (dias > 10), los primeros 10 días cuestan a $5 ($50 acumulados) y cada día a partir del 11 cuesta $10.
# La multa máxima acumulada no puede exceder los $200.00.
# ALGORITMO
# 1. Leer los días de retraso.
# 2. Si dias <= 10:
#      multa = dias * 5.0
# 3. En caso contrario:
#      multa = (10 * 5.0) + ((dias - 10) * 10.0)
# 4. Si multa > 200.0:
#      multa = 200.0
# 5. Mostrar la multa usando tabulate.
# CASOS DE PRUEBA
# 0 -> 0.00
# 10 -> 50.00
# 11 -> 60.00
# 25 -> 200.00
# 40 -> 200.00
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# La única biblioteca permitida es tabulate. No importes ningún otro módulo.
# No agregues clases, funciones auxiliares adicionales.
# No agregues validaciones, mensajes extra que no estén aquí.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerDias() -> int
# calcularMulta(dias: int) -> float
# mostrarMulta(dias: int, multa: float) -> None

from tabulate import tabulate

def leerDias():
    return int(input("Ingrese los días de retraso: "))

def calcularMulta(dias):
    if dias <= 10:
        multa = dias * 5.0
    else:
        multa = (10 * 5.0) + ((dias - 10) * 10.0)
    
    if multa > 200.0:
        multa = 200.0
    return multa

def mostrarMulta(dias, multa):
    filas = [
        ["Días de retraso", dias],
        ["Multa total", f"${multa:.2f}"]
    ]
    print(tabulate(filas, headers=["Concepto", "Valor"]))