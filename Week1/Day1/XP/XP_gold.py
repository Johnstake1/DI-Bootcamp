#EX1
print('Hello World\n'*4 + 'I love Python\n'*4)

#EX2
MONTH = int(input('input a month (1 to 12)'))

if MONTH >= 3 and MONTH <=5:
    print('You chose Spring')
elif MONTH >= 6 and MONTH <= 8:
    print('You chose Summer')
elif MONTH >= 9 and MONTH  <= 11:
    print('You chose Autumn')
elif MONTH <= 2 or MONTH == 12:
    print('You chose Winter')
else:
    print('You made a mistake')