import datetime as datetime
import calendar

import fileManager as fm


def get_dias_restantes_til_month_end():
    now = datetime.datetime.now()
    days = calendar.monthrange(now.year, now.month)[1]
    current_day = now.day
    return days - current_day


def saldo_para_mes():
    print(f" \n Faltan " + get_dias_restantes_til_month_end() +
          " dias para que termine el mes \n")
    saldo_actual = fm.get_diff_ing_gastos()
    print(" \n El saldo para cada día del mes es de $ {:,.2f} \n".format(
        round(saldo_actual / get_dias_restantes_til_month_end(), 0)))
