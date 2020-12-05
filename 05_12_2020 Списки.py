#СПИСКИ - LIST

#СОЗДАНИЕ
myDogs = []
myCats = [ 'Bonya']
myRats = ['Busia', 'Raul', 'Ron']
myStuff = ["Axaxaxaxxa", 536, True, myCats]

myShoppingList = []

#Как получить элемент списка
print(myRats[1])  #Второй с начала (отсчёт с 0)
print(myRats[-3]) #Третий с конца
print(myRats[-1]) #Последний
print(myStuff[1] > 100)


#Как изменить список
myStuff[1] = 3948
myStuff[1] = myStuff[1] + 2
myStuff[1] +=  1000
myStuff[1] + 1000000  #НЕ МЕНЯЕТ ЭЛЕМЕНТ
print(myStuff)

#Как добавить элемент
myStuff.append("Good") #Добавить в конец
myStuff.append(65)
myStuff.append(False)
myStuff.append(myRats)
print(myStuff)

#Как удалить элемент
myStuff.pop()  # Удалить последний элемент
print(myStuff)
myStuff.pop(3) # Удалить элемент с индексом 3
print(myStuff)
