import math
# Menú de opciones
opcion = 1

print('Empanadas don machetero')
print('*****')
print('0. salir')
print('1. Encontrar multiplo 2')
print('2. Encontrar raíz cuadrada')
print('3. Sumar +100')
print('4. Elevar a la 2')

while(opcion != 0):
    opcion=int(input('¿Qué quieres hacer hoy? '))
    if (opcion == 1):
        numero = int(input('Digite un número entero: '))
        if (numero % 2 == 0):
            print(f'El número {numero} es múltiplo de 2')
        else:
            print(f'El número {numero} no es múltiplo de 2')
    elif (opcion == 2):
        numero = int(input('Digite un número entero: '))
        print(f'La raíz cuadrada de {numero} es: {math.sqrt(numero)}')
    elif (opcion == 3):
        numero = int(input('Digite un número entero: '))
        print(f'La suma de {numero} + 100 es: {numero + 100}')
    elif (opcion == 4):
        numero = int(input('Digite un número entero: '))
        print(f'El cuadrado de {numero} es: {numero * numero}')
    elif (opcion == 0):
        print(f'Has salido del programa')
    else:
        print('Digita una opción válida')
        
    
else: 
    print('Saliste del programa')