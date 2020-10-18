lucky_numbers = [45,5,2,9,8,6]
# print(lucky_numbers)
lucky_numbers.insert(1,37) #inserta el elemento 37 en la posicion 1
# print(lucky_numbers)
# lucky_numbers.clear() #limpia la lista
# print(lucky_numbers)
print(lucky_numbers.index(2))#conocer el index del elemento 2

lucky_numbers.sort() #ordena de manera ascendente
lucky_numbers.reverse() #invierte el orden de una lista

lucky_numbers2 = lucky_numbers.copy() #crea una copia de la lista lucky_numbers y la guarda en lucky_numbers2