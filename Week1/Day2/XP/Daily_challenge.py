#Challenge 1

# number = int(input('Give me a number'))
# lenght = int(input('Give me a lenght'))

# multiples = []

# for i in range(1, lenght + 1):
#     multiples.append(number * i)

# print(multiples)

#Challenge 2

user_string = input('Give me a word')
new_string = ''

for i in range(len(user_string)):
    character = user_string[i]

    if i == 0 or character != user_string[i-1]:
        new_string += character

print(new_string)

