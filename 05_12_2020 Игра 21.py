from random import randint




#####
print("добро пожаловать в игру 21")
n = int(input("Сколько игроков будет?\t"))  
print()

players = ["rtrte", "werw", "wrgwegw"]

for i in range(n):  #НОВЫЙ ЦИКЛ FOR
    name = input("Введите имя " +str(i+1)+"-го игрока:\t" )
    ##HW Добавить имена игроков в список


points = [] #Сколько очков набрал каждый игрок
for j in range(n):
    random_points = randint(1, 10)
    ##HW Записать рандомное число в список points
    print(players[j], "Ваш счёт:", random_points)
    
