def guardar_agenda(l_agenda, **kwargs):
    resultado = l_agenda[:]
    resultado.append(kwargs)
    return resultado

def run():
    agenda = []
    cantidad = int(input("¿Cuantos contactos vas a introducir?"))
    for i in range(cantidad):
        contacto = {}
        contacto["nombre"] = input("Indica el nombre: ")
        contacto["telefono"] = input("Indica el telefono: ")
        campo = input("Introduzca otro campo: ")
        while campo != "*":
            contacto[campo] = input("Introduzca valor: ")
            campo = input("Introduzca otro campo: ")
            agenda = guardar_agenda(agenda, **contacto)[:]

if __name__ == '__main__':
    run()