import math, time as tm

yes = 'yes'
Yes = 'Yes'
no = 'no'
No = 'No'
a = 'a'
b = 'b'
c = 'c'

def startup ():
    print('Simple Pythagorean Solver')
startup()

def nm():
    '''
    This is where the meat of the code is located
    '''
    name = ''
    while name == '':
        tm.sleep(2)
        name = input('What is your name? ')
        is_name = input(f'Is this name correct, {name}?')
        if is_name == Yes or is_name == yes:
            ''
        else:
            name = input('What is your name? ')
    print(f'Nice to meet you {name}')

    solve = input(f'Let\'s get started solving some Pythagreom Theroem, then {name} '
                  f'\n Would you like to solve for a, b, or c? ')

    if solve == a or solve == a.capitalize():
        length_b = int(input('What is the length of b?'))
        length_c = int(input('What is the length of c?'))
        length_b = length_b * length_b
        length_b = str(length_b)
        length_c = length_c * length_c
        length_c = str(length_c)
        print(f' So once we square side B the length is {length_b} and Side C is {length_c} ')
        length_b = int(length_b)
        length_c = int(length_c)
        length_a = length_c - length_b
        length_a = math.sqrt(length_a)
        length_b = math.sqrt(length_b)
        length_c = math.sqrt(length_c)
        length_a = str(length_a)
        length_b = str(length_b)
        length_c = str(length_c)
        print(f'Length A is equal to {length_a}, Length B is equal to {length_b}, Length C is equal to {length_c}')
    elif solve == b or solve == b.capitalize():
        length_a = int(input('What is the length of a?'))
        length_c = int(input('What is the length of c?'))
        length_a = length_a * length_a
        length_a = str(length_a)
        length_c = length_c * length_c
        length_c = str(length_c)
        print(f' So once we square side A the length is {length_a} and Side C is {length_c} ')
        length_a = int(length_a)
        length_c = int(length_c)
        length_b = length_c - length_a
        length_b = math.sqrt(length_b)
        length_a = math.sqrt(length_a)
        length_c = math.sqrt(length_c)
        length_a = str(length_a)
        length_b = str(length_b)
        length_c = str(length_c)
        print(f'Length A is equal to {length_a}, Length B is equal to {length_b}, Length C is equal to {length_c}')
    elif solve == c or solve == c.capitalize():
        length_a = int(input('What is the length of a?'))
        length_b = int(input('What is the length of b?'))
        length_a = length_a * length_a
        length_a = str(length_a)
        length_b = length_b * length_b
        length_b = str(length_b)
        print(f' So once we square side A the length is {length_a} and Side B is {length_b} ')
        length_a = int(length_a)
        length_b = int(length_b)
        length_c = length_a + length_b
        length_b = math.sqrt(length_b)
        length_a = math.sqrt(length_a)
        length_c = math.sqrt(length_c)
        length_a = str(length_a)
        length_b = str(length_b)
        length_c = str(length_c)
        print(f'Length A is equal to {length_a}, Length B is equal to {length_b}, Length C is equal to {length_c}')
    else:
        print('Sorry this was not a correct choice.')


nm()

def goodbye():
    tm.sleep(10)
    print('Thanks for using!!')
    tm.sleep(10)
goodbye()


