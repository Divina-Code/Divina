my_shopping_list = []

while True:
    answ = input("""
Что вы хотите сделать?
Добавить продукт в список - ADD,
Показать список - SHOW\n""")

    if answ == "SHOW":
        print(my_shopping_list)
    elif answ == "ADD":
        item = input("Что вы хотите добавить?\t")
        my_shopping_list.append(item)

        
    else:
        print(" не понял твою команду")
