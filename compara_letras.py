def run():
    letra = input("Ingresa caracter: ")
    if letra >= "A" and letra <= "Z":
        print("Es Mayuscula")
    elif letra >= "a" and letra <= "z":
        print("Es Minuscula")
    else:
        print("Es Otro caracter")

if __name__ == '__main__':
    run()