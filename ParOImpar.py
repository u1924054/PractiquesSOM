
#Programa per treballar modul, condicionals i igualtat

numero = int(input('Introdueix un numero'))
if numero%2==0: #El numero es par
    print('El numero es parell')
else: #El numero es imparell
    print('El numero es imparell')

if numero%4==0:
    print('El numero es multiple de 4')

#numero para para verificar 
num = int(input('Introdueix un numero per verificar'))
check = int(input('Introdueix un numero per dividir'))
if check%num == 0:
    print('Check divideix uniformament en num')
else:
    print('Chek no divideix uniformament en num')