from random import randint

print("Welcome!")
name = input("What is your name?   ")
print("Hello,", name)

gameover = False
computer_number = randint(1, 100)
#print(computer_number)

lives = 7


while gameover != True:
    print()
    a = int(input("Enter your number: ")) 

    if a == computer_number:
        print("PERFECT")
        gameover = True
        
    if a > computer_number:
        lives = lives - 1
        print("Too big", lives)
        
        
    if a < computer_number: 
        lives = lives - 1
        print("To small", lives)

    if lives == 0:
        print("You loose!")
        print("Number is", computer_number)
        gameover = True




        
    
