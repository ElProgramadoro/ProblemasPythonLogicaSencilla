#este programa obtiene nombre y edad y lo devuelve con formato
def datos(name,age):
    return(print(f'Hola {name}, tu edad es {age}'))

datos(name=input('Inserte su nombre: '), age=int(input('Inserte su edad: ')))