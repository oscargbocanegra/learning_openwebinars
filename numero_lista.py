num = int(input("Numero: "))
lista = []
while num>0:
    lista.append(num)
    num = int(input("Numero: "))
print(f'Maximo: {max(lista)}')
for n in lista:
    print(n, end=' ')
print()
