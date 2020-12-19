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
for j in range(n):
    random_points = randint(1, 10)
    points.append(random_points)
    print(players[j], "Ваш счёт:", random_points)

print("\nОЧКИ: ",points)

### ОСНОВНАЯ ИГРА НАЧИНАЕТСЯ ТУТ
game = True #Игра продолжается или закончена
while game:
    print("\n \t\t\tROUND")

    for a in range(n):
        answer = input(players[a] + ' будете брать карту? [ДА\НЕТ]')

        answer = answer.upper() #Делаем все буквы ЗАГЛАВНЫМИ
        answer = answer.strip()  #УБираем лишние пробелы, если они есть

        if answer == "ДА":
            print("Вы ответили ", answer)
            ##!!!!! Сгенерировать новое число от 1 до 10 и прибавить к счёту игрока
            ## Вывести игроку его новый счёт
        elif answer == "НЕТ":
            print("Вы ответили ", answer)
        else:
            print("Не понял твоего ответа, принимаю только 'ДА' или 'НЕТ' ")

    print("\n____________________________")
    for b in range(n): # Выводим счёт для каждого игрока
        print(players[b], "У вас очков:", points[b])
