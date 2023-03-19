#calcula el promedio de X cantidad de notas
def profe(can):
    suam = 0
    for i in range(can):
        n = (float(input(f'Ingrese la nota #{i+1} :')))
        suam += n
    return print('El promedio de notas es: ', suam/can)
can = (int(input('Cuantas notas ingresara: ')))
profe(can)