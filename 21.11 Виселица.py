from random import randint # Добавляем библиотеку случайных чисел



words  = ["австралия", "индия", "джибути", "англия", "филиппины"] #список слов

random_index = randint(0, 4) #генерируем число от 0 до 4 
word = words[random_index] #записываем в переменную word слово из списка wordS со случайным индексом

print(word)

game = True #Игра повторяется, пока эта переменная True
lives = 10 #В начале игры у игрока 10 жизней


letters = []#список угаданных букв

while game:
    print()
    print()
    print("*"+"___*"*len(word))
    letter = input("Введите букву или слово: ")

    if len(letter)<1: #нам НИЧЕГО не ввели
        print("Нужно ввести что-нибудь, букву или слово")
        
    elif len(letter) == 1: #нам ввели БУКВУ
       ##Проверяем букву
        if letter in word:
            if letter not in letters: #Если этой буквы нет в списке угаданных
                print("Есть такая буква!")            
                letters.append(letter) #Добавляем в список угаданных букв
            else:
                print("Ты уже угадывал такую букву")
                lives = lives - 1 
        else:
            print("такой буквы нет")
            lives = lives - 1    

    else: #нам ввели СЛОВО
        if letter == word:
            print("ТЫ ПОБЕДИЛ! Игра окончена")
            
        else:
            print("Не угадал! Игра окончена, ТЫ ПРОИГРАЛ")
            
        game = False    
        
          
    
    print("Осталось", lives, "жизней", "Угаданные буквы: ", letters )    
    

    #Если жизни кончились, цикл должен остановиться
    if lives == 0:
        print("У тебя кончились жизни, ты проиграл")
        game = False

    
print("Спасибо за игру, приходи ещё!")
