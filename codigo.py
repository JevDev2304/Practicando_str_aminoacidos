def obtener_lista_de_la_palabra(palabra):
    lista_palabra = []
    for caracter in palabra:
        lista_palabra.append(caracter)

    return lista_palabra


def obtener_lista_sin_valores_repetidos(lista):
    lista_sin_letras_repetidas = []
    for letra in lista:
        if letra not in lista_sin_letras_repetidas:
            lista_sin_letras_repetidas.append(letra)

    return lista_sin_letras_repetidas


def contar_repeticiones_letras_en_la_cadena(lista, lista_sin_valores_repetidos):
    lista_veces_repetido=[]
    for x in range(len(lista_sin_valores_repetidos)):
        lista_veces_repetido.append(x)

    for i in range(len(lista_veces_repetido)):
        numero_veces = 0
        for letra_a_contar in lista:
            if lista_sin_valores_repetidos[i] == letra_a_contar:
                numero_veces += 1
        lista_veces_repetido[i] = numero_veces
    return lista_veces_repetido


def calcular_porcentaje(lista):
    lista_porcentajes=[]
    for x in range(len(lista)):
        lista_porcentajes.append(x)
    for i in range(len(lista_porcentajes)):
     lista_porcentajes[i]=(lista[i]/sum(lista))*100
    return lista_porcentajes


palabra=(str(input("Ingresa el aminoacido o la vaina con letras: ")))
palabra=palabra.upper()
lista_palabra=obtener_lista_de_la_palabra(palabra)
lista_sin_valores_repetidos_para_contar=obtener_lista_sin_valores_repetidos(lista_palabra)
lista_con_repeticion=contar_repeticiones_letras_en_la_cadena(lista_palabra,lista_sin_valores_repetidos_para_contar)
lista_porcentajes=calcular_porcentaje(lista_con_repeticion)

print(f"El aminoacido o palabra rara es {palabra}\n")
for i in range(len(lista_sin_valores_repetidos_para_contar)):
    print(f"Las veces que se repite {lista_sin_valores_repetidos_para_contar[i]} en la palabra rara o aminoacido es  {lista_con_repeticion[i]} \n Y su porcentaje es {lista_porcentajes[i]} %.")
print("Regalito de juanes xd ")






