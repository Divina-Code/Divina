#ТАБЛИЦА УМНОЖЕНИЯ
#У игрока есть 3 балла вначале
#За правильный ответ дают 1, за неправильный -1
#Вопроосы генерируются автоматически
#Если набрал 10 - победил
#Дошёл до 0 - проиграл



#ПОСКАЗКА
from random import randint #ИМПОРТИРОВАЛИ МОДУЛЬ random


score = 3 #ПЕРЕМЕННАЯ Баллы в начале игры
gameover = False #ПЕРЕМЕННАЯ закончили играть или нет

while gameover != True: #Запускаем ЦИКЛ до тех пор, пока gameover не станет TRUE
    
    a = randint(1, 10) #Генерируем число от 1 до 10
    b = randint(1, 10) #Генерируем число от 1 до 10
    
    print("----------") 
    answer = int(input(str(a) + " * " + str(b) + " = "))

    if answer  == a*b:
        score = score + 1
        print("MOLODEC!")        

    else:
        score = score - 1
        print("NE PRAVIL'NO")
        
    print("TVOI SCHET:", score)

    if score == 0:
        print("YOU LOOSE")
        gameover = True
        
    if score == 10:
        print("YOU WIN")
        gameover = True    
        
