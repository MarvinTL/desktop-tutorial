from os import system

def menu1():
    print('1. Convertir entre Km y Millas')
    print('2. Convertir entre m3 y pie3')
    print('3. Convertir entre pies, mts y yardas')
    print('10. Salir')
    opcion = int(input('Ingrese su opción: '))
    return opcion

def conversion_Km_millas(conversion, distancia):
    if conversion == 'a':
        return distancia * 0.621371  # Conversión de km a millas
    elif conversion == 'b':
        return distancia * 1.60934   # Conversión de millas a km

def conversion_m3_pies(conversion, volumen):
    if conversion == 'a':
        return volumen * 35.3147  # Conversión de m3 a pies cúbicos
    elif conversion == 'b':
        return volumen / 35.3147  # Conversión de pies cúbicos a m3

def conversion_pies_metros_yardas(conversion, distancia):
    if conversion == 'a':
        return distancia * 0.3048  # Conversión de pies a metros
    elif conversion == 'b':
        return distancia * 3.28084  # Conversión de metros a pies
    elif conversion == 'c':
        return distancia * 0.9144  # Conversión de yardas a metros
    elif conversion == 'd':
        return distancia * 1.09361  # Conversión de metros a yardas

while True:
    system('cls')
    op = menu1()
    
    if op == 1:
        conv = input('Escriba a para km a millas, y b para millas a km: ')
        conv = conv.lower()
        if conv != 'a' and conv != 'b':
            print('Debe elegir una opción válida')
        else:
            cant = float(input('Ingrese la cantidad: '))
            de_a = conversion_Km_millas(conv, cant)
            if conv == 'a':
                print(f'{cant} km son {de_a} millas')
            else:
                print(f'{cant} millas son {de_a} km')
            system('pause')
    
    elif op == 2:
        conv = input('Escriba a para m3 a pies cúbicos, y b para pies cúbicos a m3: ')
        conv = conv.lower()
        if conv != 'a' and conv != 'b':
            print('Debe elegir una opción válida')
        else:
            cant = float(input('Ingrese la cantidad: '))
            de_a = conversion_m3_pies(conv, cant)
            if conv == 'a':
                print(f'{cant} m3 son {de_a} pies cúbicos')
            else:
                print(f'{cant} pies cúbicos son {de_a} m3')
            system('pause')
    
    elif op == 3:
        conv = input('Escriba a para pies a metros, b para metros a pies, c para yardas a metros, y d para metros a yardas: ')
        conv = conv.lower()
        if conv not in ['a', 'b', 'c', 'd']:
            print('Debe elegir una opción válida')
        else:
            cant = float(input('Ingrese la cantidad: '))
            de_a = conversion_pies_metros_yardas(conv, cant)
            if conv == 'a':
                print(f'{cant} pies son {de_a} metros')
            elif conv == 'b':
                print(f'{cant} metros son {de_a} pies')
            elif conv == 'c':
                print(f'{cant} yardas son {de_a} metros')
            elif conv == 'd':
                print(f'{cant} metros son {de_a} yardas')
            system('pause')
    
    elif op == 10:
        break
    
    else:
        print('Debe elegir una opción válida')
        system('pause')