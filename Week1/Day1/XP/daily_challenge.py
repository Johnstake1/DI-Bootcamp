#EX1

INPUT = input('Write a word')
if len(INPUT) < 10:
    print('string not long enough')
elif len(INPUT) > 10:
    print('string too long')
elif len(INPUT) == 10:
    print('perfect string')

#EX2
INPUT2 = input('Type Hello World')
HW = 'Hello World'
if INPUT2 == HW:
    print(HW[0])
    print(HW[10])

#EX3

result = ''
for char in INPUT:
    result += char
    print(result)


###

# Juliana's solution for EX4

import random
user_input= list('Hello World')
print(user_input)
random.shuffle(user_input)
print(user_input)
print(''.join(user_input))
