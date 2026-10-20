# PROBLEMA
# Calcular la comisión por ventas de un vendedor, su bono e importe total a pagar según sus ventas mensuales.
# ENTRADAS
# ventas: float, pesos, mayor o igual a 0.
# SALIDAS
# comision: float, pesos, formato con dos decimales.
# bono: float, pesos, formato con dos decimales.
# total: float, pesos, formato con dos decimales, mostrado en tabla usando tabulate.
# REGLAS Y SUPUESTOS
# Comisión base: 5% sobre las ventas (ventas * 0.05).
# Si las ventas son de $10,000 o más (ventas >= 10000), la comisión es de 8% (ventas * 0.08).
# Si las ventas son de más de $50,000 (ventas > 50000), recibe además un bono fijo de $1,000.00.
# ALGORITMO
# 1. Leer las ventas.
# 2. Si ventas > 50000:
#      comision = ventas * 0.08
#      bono = 1000.0
# 3. En caso contrario, si ventas >= 10000:
#      comision = ventas * 0.08
#      bono = 0.0
# 4. En caso contrario:
#      comision = ventas * 0.05
#      bono = 0.0
# 5. Calcular total = comision + bono
# 6. Mostrar comisión, bono y total usando tabulate.
# CASOS DE PRUEBA
# 5000 -> Com: 250.00, Bono: 0.00, Total: 250.00
# 10000 -> Com: 800.00, Bono: 0.00, Total: 800.00
# 50000 -> Com: 4000.00, Bono: 0.00, Total: 4000.00
# 50001 -> Com: 4000.08, Bono: 1000.00, Total: 5000.08
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# La única biblioteca permitida es tabulate. No importes ningún otro módulo.
# No agregues clases, funciones auxiliares adicionales.
# No agregues validaciones, mensajes extra que no estén aquí.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerVentas() -> float
# calcularComision(ventas: float) -> float
# calcularBono(ventas: float) -> float
# mostrarPago(ventas: float, comision: float, bono: float) -> None

from tabulate import tabulate

def leerVentas():
    return float(input("Ingrese el total de ventas del mes: "))

def calcularComision(ventas):
    if ventas >= 10000:
        comision = ventas * 0.08
    else:
        comision = ventas * 0.05
    return comision

def calcularBono(ventas):
    if ventas > 50000:
        bono = 1000.0
    else:
        bono = 0.0
    return bono

def mostrarPago(ventas, comision, bono):
    total = comision + bono
    filas = [
        ["Ventas", f"${ventas:.2f}"],
        ["Comisión", f"${comision:.2f}"],
        ["Bono", f"${bono:.2f}"],
        ["Total a pagar", f"${total:.2f}"]
    ]
    print(tabulate(filas, headers=["Concepto", "Valor"]))