#este programa toma la edad del usuario y valida si puede votar o no
def voto(edad):

    if edad > 17:
        print('usted puede votar')
    elif edad < 18:
        print('usted no puede votar')
while(True):
    try:
        voto(edad=int(input('inserte su edad: ')))
        break
    except:
        ValueError(print('Ingrese una edad en numero'))   