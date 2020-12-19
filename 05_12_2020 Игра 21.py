from random import randint

#####
print("добро пожаловать в игру 21")
n = int(input("Сколько игроков будет?\t"))
print()

###Записываем имена игроков в список
players = []  # Список имён игроков СТРОКА
points = []  # Сколько очков набрал каждый игрок ЧИСЛО
playORnot = []  # Продолжает игрок или нет TRUE/FALSE

for i in range(n):  # цикл повторяется столько раз, сколько у нас игроков
    # ИМЯ
    name = input("Введите имя " + str(i + 1) + "-го игрока:\t")
    players.append(name)  # Добавляем имя в список

    # ОЧКИ
    random_points = randint(1, 10) #Генерируем рандоммное число
    points.append(random_points) #добавляем в список points

    # ИГРАЕТ ИЛИ НЕТ
    playORnot.append(True)

for i in range(n):  # Выводим счёт для каждого игрока
    print(players[i], "У вас очков:", points[i])

### ОСНОВНАЯ ИГРА НАЧИНАЕТСЯ ТУТ

while playORnot.count(True) > 0:
    print("\n \t\t\tROUND")

    for i in range(n):
        print()
        if playORnot[i] == True:
            answer = input(players[i] + ' будете брать карту? [ДА\НЕТ]')

            answer = answer.upper()  # Делаем все буквы ЗАГЛАВНЫМИ
            answer = answer.strip()  # УБираем лишние пробелы, если они есть

            if answer == "ДА":
                random_points = randint(1, 10)
                points[i] += random_points
                print(players[i], "Вам выпало:", random_points)

                if points[i] >= 21:
                    playORnot[i] = False
                    ###Если игрок набрал 21 очко или больше, то он выбывает из игры



            elif answer == "НЕТ":
                print("Вы ответили ", answer)
                playORnot[i] = False
            else:
                print("Не понял твоего ответа, принимаю только 'ДА' или 'НЕТ' ")

    print("\n____________________________")
    for i in range(n):  # Выводим счёт для каждого игрока
        print(players[i], "У вас очков:", points[i])
