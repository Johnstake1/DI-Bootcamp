#Ex1

print('hello world\n'*4)

#EX2
EX2 = (99**3)*8
print(EX2)

#EX3
5 < 3 #FALSE
3 == 3 #TRUE
3 == "3" #FALSE
#"3" > 3 #ERROR str-int
'Hello' == 'hello' #FALSE

#EX4
COMPUTER_BRAND = 'Lenovo'
print(f'I have a {COMPUTER_BRAND} computer')

#EX5
NAME = 'Jonathan'
AGE = 35
SHOE_SIZE = 41
INFO = f'my name is {NAME}, I am {AGE} years old. My shoe size is {SHOE_SIZE}'
print(INFO)

#EX6
A = 10
B = 1


if A > B:
    print('Hello World')

#EX7
ASK = int(input('Submit a number'))
if ASK %2 == 0:
    print('You chose an even number')
else:
    print('You chose an odd number')

#EX8

NAME1 = input('What is your name?? ')
if NAME1 == NAME:
    print('Hola Tocayou')
else:
    print('Suerte la proxima')

#EX9
HEIGHT = int(input('What is your height expressed in cm? '))
if HEIGHT > 145:
    print('You can ride the rollercoaster')
else:
    print('You need to grow a few inches')