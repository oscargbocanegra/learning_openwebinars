from ast import Return
from typing import Type


def calcular_segundos(horas,minutos,segundos):
    return horas * 3600 + minutos * 60 + segundos

def calcular_horas(segundos):
    horas = segundos // 3600
    segundos -= horas * 3600
    minutos = segundos // 60
    segundos -= minutos * 60
    return horas,minutos,segundos

def calcular(*args):
    if len(args) == 1:
        return calcular_horas(args[0])
    elif len(args) ==3:
        return calcular_segundos(*args)
    else:
        raise TypeError("Se espera 1 0 3 parametros")

def run():
    print(calcular(4,12,23))
    print(calcular(12345))


    # print(calcular_segundos(4,12,23))
    # hora = map(str, calcular_horas(12345))
    # print(":".join(hora))

if __name__ == '__main__':
    run()