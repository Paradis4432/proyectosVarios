import pandas as pd
import fileManager as fm


def action1():
    ingGlobal = None
    while True:
        print("Ingresos\n1. Agregar ingreso\n2. Ver ingresos\n3. Regresar")
        accion1 = input("Ingrese una opción: ")
        if accion1 == "1":
            print("Ingrese los datos del ingreso")
            monto = input("Monto: ")
            concepto = input("Concepto: ")
            estado = input("Estado: ")

            ingresos = pd.read_csv("ingresos.csv", sep=";")

            nuevo_ingreso = pd.DataFrame(
                {"monto": [monto], "concepto": [concepto], "estado": [estado]})

            ingresos = ingresos.append(nuevo_ingreso, ignore_index=True)

            print("Ingreso registrado")
            ingresos.to_csv("ingresos.csv", sep=";")
            ingGlobal = ingresos

        elif accion1 == "2":
            print(ingGlobal)
            print("Total de ingresos: $ {:,.2f}".format(
                round(fm.get_total_ingresos())))

        elif accion1 == "3":
            break
        else:
            print("Opción inválida")


def action2():
    egrGlobal = None
    while True:
        print("Egresos\n1. Agregar egreso\n2. Ver egresos\n3. Regresar")
        accion2 = input("Ingrese una opción: ")
        if accion2 == "1":
            print("Ingrese los datos del egreso")
            monto = input("Monto: ")
            concepto = input("Concepto: ")
            estado = input("Estado: ")

            egresos = pd.read_csv("egresos.csv", sep=";")

            nuevo_egreso = pd.DataFrame(
                {"monto": [monto], "concepto": [concepto], "estado": [estado]})

            egresos = egresos.append(nuevo_egreso, ignore_index=True)

            print("Egreso registrado")
            egresos.to_csv("egresos.csv", sep=";")
            egrGlobal = egresos

        elif accion2 == "2":
            print(egrGlobal)
            print("Total de egresos: $ {:,.2f}".format(
                round(fm.get_total_egresos())))

        elif accion2 == "3":
            break

def action4():
    while True:
        print("Proponer gasto\n1. Proponer gasto\n2. salir")
        option = input("Ingrese una opción: ")

        if option == "1" or option == "2":
            break
        print("Opción inválida")