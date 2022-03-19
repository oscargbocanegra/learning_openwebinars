import os
def run():
    secreto = int(input('Numero secreto: '))
    os.system("clear")
    cont=1
    num = int(input('Numero: '))

    while num!= secreto:
        if num> secreto:
            print('El numero es Menor')
        else:
            print('El numero es Mayor')
        cont+=1
        num = int(input('Numero: '))
    print(f'Ganaste con {cont} intentos')

if __name__ == "__main__":
    run()