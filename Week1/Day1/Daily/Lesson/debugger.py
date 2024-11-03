age = int(input('How old are you?'))
print(f'You are {age} years old')

if age > 18 and age < 35:
    print('You can enter the club')
elif age < 18 and age > 12:
    print('You are a teenager')
else:
    print('You are an adult')