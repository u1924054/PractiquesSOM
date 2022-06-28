# crear una llista de numeros i imprimir nomes els menors de 5 

numbers = [7, 3, 13, 6, 8, 5, 1, 2, 4, 15, 9, 10, 12, 14, 11]
newList = [] #creem array buida
newList2 = []
for x in numbers:
   if x<5:
     newList.append(x) # afegir a la llista
     newList.sort() # ordenar la llista de menor a major 
#final del for

#mostrar llista
print(newList)

#Entrar un numero per teclat

num = int(input('Ingresa un nou numero: '))
for x in numbers:
    if x<num:
        newList2.append(x)
        newList2.sort() # ordenar la llista de menor a major

print(newList2)