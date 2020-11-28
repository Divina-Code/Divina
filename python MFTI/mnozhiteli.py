from random import choice

nums = [2, 3, 4, 5, 6, 8, 9, 11, 13, 17]

n = 1

for i in range(5):
    n*= choice(nums)

print(n)    
