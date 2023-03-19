#Este programa solicita un numero e imprime el cuadrado y el cubo
def p1(num):
    for a in range(num+1):
        res1=a**2
        res2=a**3
        print(f'Numero: {a} Cuadrado:{res1} Cubo:{res2}')
        
num=int(input('Ingrese un numero:'))
p1(num)