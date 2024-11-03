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