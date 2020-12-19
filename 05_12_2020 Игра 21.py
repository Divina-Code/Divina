from random import randint



#####
print("добро пожаловать в игру 21")
n = int(input("Сколько игроков будет?\t"))  
print()

###Записываем имена игроков в список
players = [] #Список имён игроков
for i in range(n):  #НОВЫЙ ЦИКЛ FOR
    name = input("Введите имя " +str(i+1)+"-го игрока:\t" )
    players.append(name) #Добавляем имя в список

print("\nИГРОКИ: ", players)


### Генерируем каждому игроку его стартовый счёт
points = [] #Сколько очков набрал каждый игрок
for i in range(n):
    random_points = randint(1, 10)
    points.append(random_points)
    print(players[i], "Ваш счёт:", random_points)

print("\nОЧКИ: ",points)


###Продолжает игрок или нет
playORnot = []
for i in range(n):
    playORnot.append(True)
    #Добавилли True столько раз, сколько у нас игроков

### ОСНОВНАЯ ИГРА НАЧИНАЕТСЯ ТУТ

while playORnot.count(True) >0:
    print("\n \t\t\tROUND")

    for i in range(n):
        if playORnot[i] == True:
            answer = input(players[i] + ' будете брать карту? [ДА\НЕТ]')

            answer = answer.upper() #Делаем все буквы ЗАГЛАВНЫМИ
            answer = answer.strip()  #УБираем лишние пробелы, если они есть

            if answer == "ДА":
                print("Вы ответили ", answer)
                random_points = randint(1, 10)
                points[i]+=random_points
                print(players[i], "Вам выпало:", random_points)

                if points[i] >=21:
                    playORnot[i] = False
                    ###Если игрок набрал 21 очко или больше, то он выбывает из игры


                ##!!!!! Сгенерировать новое число от 1 до 10 и прибавить к счёту игрока
                ## Вывести игроку его новый счёт
            elif answer == "НЕТ":
                print("Вы ответили ", answer)
                playORnot[i] = False
            else:
                print("Не понял твоего ответа, принимаю только 'ДА' или 'НЕТ' ")

    print("\n____________________________")
    for i in range(n): # Выводим счёт для каждого игрока
        print(players[i], "У вас очков:", points[i])
