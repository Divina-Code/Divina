from random import randint # Добавляем библиотеку случайных чисел



word = "австралия"

game = True

while game:
    print()
    
    letter = input("Введите букву или слово: ")

    if letter == word:
        print("ТЫ ПОБЕДИЛ! Игра окончена")
        game = False
        
    elif letter in word:
        print("Есть такая буква!")
        
    else:
        print("Не подходит")
