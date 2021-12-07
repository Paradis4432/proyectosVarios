import numpy as np
import pandas as pd

import timeG as tg

egresos = pd.read_csv("egresos.csv", sep=";")
ingresos = pd.read_csv("ingresos.csv", sep=";")


def get_total_egresos():
    return egresos["monto"].sum()


def get_total_ingresos():
    return ingresos["monto"].astype(int).sum()


def get_diff_ing_gastos():
    return get_total_ingresos() - get_total_egresos()

def get_saldo_actual():
    #imprime texto en la consola que indique que esta cargando
    print("\nCargando... \n")
    print("\n Saldo actual: $ {:,.2f}\n".format(round(get_total_ingresos(),0)))
    tg.saldo_para_mes()