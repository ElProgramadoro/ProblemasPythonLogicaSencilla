#tabla de multiplicar
def tabla(num):
    i = 0
    while i < 12:
        i+=1        
        print(f'{num} x {i} = ',num*i)

tabla(num=int(input('Ingrese un numero:')))
