numero = int(input('Ingresa un valor positiu: '))
# crear una lista amb numero elements desde 0
list = range(1, numero+1)
#llista buida per al divisors de numero 
llistaDeDivisors = []

print('Divisors de ', numero, ': ')
for element in list:
    if numero % element == 0:
        llistaDeDivisors.append(element)

#mostrar llista

print(llistaDeDivisors)
