contador = 1
sumatoria = 0

while (contador <= 5):
    numero = int(input('Digita un número: '))
    if (numero < 0):
        sumatoria += 1
    contador += 1
print(f'La cantidad de números negativos ingresados fueron: {sumatoria}')