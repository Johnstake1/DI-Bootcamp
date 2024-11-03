#Basic Data Types: strings; integers; float; boolean

some_variable = 15
some_variable_2 = 2.2
my_name = 'Jonathan'
my_bool = True
print(type(my_name))
print(type(some_variable))
print(type(some_variable_2))
print(type(my_bool))



#STRINGS
greetings = 'Shabat Shalom'

#indexing a string
print(greetings[3])
#slicing a strign
print(greetings[2:4]) #returns 'al'
print(greetings[2:5]) #returns 'alo'
print(greetings[2:]) #returns from position 2 to the end of the string

#Strings most used methods
print(len(greetings)) #measures the lenght of the string
print(greetings[2:len(greetings)]) #returns from position to until the lenght of the string.
print(greetings[-1]) #returns the last position in the string

#string methods
print('hello'.capitalize())
print(greetings.title())
print(greetings.replace('Shalom', 'Meburach'))

greetings_new = greetings.replace('Shalom', 'Meburach')

print(greetings)
print(greetings_new)

student = '  Harry Potter  '
student = student.strip()
print(student + greetings)
print(student + " " + greetings)

#\n it will jump a line 
# \t it will tabulate


#NUMBERS: integer, float, complex numbers, boolean
int_num = 5 #int: whole numbers
float_num = 1.2

#OPERATIONS
print(int_num + float_num)

print(greetings *10)
#\n it will jump a line 
# \t it will tabulate

print(round(5/3, 2))
print(11//2)
print(11%2)
print(1625%5)

if 12%3 == 0:
    print('Yes!')


my_age = 35
new_age = 123879
my_new_age = my_age + new_age

print(my_new_age)

my_age = int(input('What is your age?')) # we add the int since the inputs are always strings
print(type(my_age))

if my_age <18:
    print('You can\'t drink vodka')
else:
    print('Let\'s celebrate')

#COMPARISON OPERATORS
print(5 <= 7)
print(5 == 5)

#Adding data types together

first_name = 'Hermione'
last_name = 'Granger'

print('Hello' + first_name + '' + last_name + '', 'Welcome to Hogwarts')

#f string
print(f'Hello {first_name} {last_name}, Welcome to Hogwarts')

print ('python' is 'python') #comparison
print('python' is not 'python')
print('HTML' is not 'CSS' and 'Python' is 'Javascript')

if 'HTML' is not 'CSS' and 'Python' is 'Javascript':
    print('That\'s right!')
