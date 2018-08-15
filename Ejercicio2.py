print('Operaciones Aritmeticas')
num1 = input('Ingrese el primer numero: ')
num2 = input('Ingrese el segundo numero: ')
print('Menu de operaciones')
print('1. Sumar numeros')
print('2. Restar numeros')
print('3. Multiplicar numeros')
print('4. Dividir numeros')
opc = input('Digite la operacion a realizar: ')


def suma(n,m):
    result= n+m
    return result
def resta(n,m):
    result = n-m
    return result

def multi(n,m):
    result = n*m
    return result

def div(n,m):
    result = n/m
    return result

if int(opc)== 1:
    resu = suma(int(num1),int(num2))
    print('La suma de los numeros es: {}'.format(resu))
elif int(opc) == 2:
    resu = resta(int(num1),int(num2))
    print('La resta de los numeros es: {}'.format(resu))
elif int(opc) == 3:
    resu = multi(int(num1),int(num2))
    print('La multiplacion de los numeros es: {}'.format(resu))
elif int(opc) == 4:
    resu = div(int(num1),int(num2))
    print('La division de los numeros es: {}'.format(resu))
else:
    print('Ha digitado una opcion incorrecta')
