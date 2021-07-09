import random
import time as tm
'''
The point of this program is to ask the user for two numbers. Then, the program will create a spread between the two numbers given.
Ex. num1 = 22, num2 = 99, random num1= 30, random num2 = 82, spread = 52 

'''
print(
    'This program will randomly choose two numbers and and you will choose the range for the numbers \n \n PLEASE USE INTEGRERS ONLY!!'
)
rand_int1 = int(input('\n Please print your first number? '))
rand_int2 = int(input('Please print your second number? '))
if rand_int1 > rand_int2:
    print('Your first number was greater than yoursecond number...')
    print('Please choose another number...')
    del rand_int2
    rand_int2 = int(input())

number1 = rand_int1 - 1
number1 = random.randint(rand_int1, rand_int2)
number2 = rand_int2 - 1
number2 = random.randint(rand_int1, rand_int2)
if number1 > number2:
    number = number1 - number2
    print(
        f'The diffrence between your {number} \n and your 1st number was {number1} \n and your second number was {number2}'
    )
elif number2 > number1:
    number = number2 - number1
    print(
        f' The diffrence between your {number} and your 2nd number was {number2} and your 1st number was {number1} '
    )
else:
    print(f'Your numbers are the same mate {number2}, {number1}')
