def run():
    dic = {}
    frase = input("Frase: ")
    lista_palabras = frase.split(" ")
    for palabra in lista_palabras:
        if palabra in dic:
            dic[palabra] += 1
        else:
            dic[palabra] = 1
    
    for campo, valor in dic.items():
        print(campo, "->", valor)
    

if __name__ == '__main__':
    run()