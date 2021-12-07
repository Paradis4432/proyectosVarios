import pandas as pd

from datetime import date
import calendar
import datetime

import fileManager as fm
import consoleManager as cm

accion = input(
    "Qué desea hacer? \n 1. Ingresos \n 2. Egresos \n 3. Saldos \n 4. Proponer Gasto \n 5. Salir \n")

while accion != "5":
    if accion == "1":
        cm.action1()
    elif accion == "2":
        cm.action2()
    elif accion == "3":
        fm.get_saldo_actual()
    elif accion == "4":
        cm.action4()
    elif accion == "5":
        break
    else:
        print("Ingrese una opción correcta")
    accion = input(
        "Qué desea hacer? \n 1. Ingresos \n 2. Egresos \n 3. Saldos \n 4. Salir \n")

print("Hasta luego")

#print("El total de tus ingresos es de ${:,.2f}".format(round(total_ingresos(),0)))
#print("El total de tus egresos es de ${:,.2f}".format(round(total_egresos(),0)))
