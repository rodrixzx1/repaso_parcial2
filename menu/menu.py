from ejercicios import ejercicio1_taxi as ej1
from ejercicios import ejercicio2_comision as ej2
from ejercicios import ejercicio3_biblioteca as ej3

def ejecutarEjercicio1():
    km = ej1.leerKilometros()
    importe = ej1.calcularImporte(km)
    ej1.mostrarImporte(km, importe)

def ejecutarEjercicio2():
    ventas = ej2.leerVentas()
    comision = ej2.calcularComision(ventas)
    bono = ej2.calcularBono(ventas)
    ej2.mostrarPago(ventas, comision, bono)

def ejecutarEjercicio3():
    dias = ej3.leerDias()
    multa = ej3.calcularMulta(dias)
    ej3.mostrarMulta(dias, multa)

def mostrarMenu():
    print()
    print("PRÁCTICA DE REPASO: EXAMEN PARCIAL")
    print("1. Viaje en taxi")
    print("2. Comisión de ventas")
    print("3. Multa de biblioteca")
    print("0. Salir")

def menus():
    opcion = ""
    while opcion != "0":
        mostrarMenu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ejecutarEjercicio1()
        elif opcion == "2":
            ejecutarEjercicio2()
        elif opcion == "3":
            ejecutarEjercicio3()
        elif opcion != "0":
            print("Opción no válida.")