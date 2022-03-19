from functools import reduce
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
def sqr(x): return x **2
mapper = list(map(sqr, lista))
print(f'Imprimiendo la funcion map {mapper}')

def par(x): return x % 2 == 0
filt = list(filter(par, lista))
print(f'Imprimiendo la funcion filter {filt}')

def add(x,y): return x + y
reducer = reduce(add, lista)
print(f'Imprimiendo la funcion reduce {reducer}')