#FUNCTIONS
#Syntax

# def say_hello():
#     print('Hello Python')

# #CALLING THE FUNCTION
# say_hello()
# #ARGUMENT
# def say_hello(greeting):
#     print(f'{greeting} Python')

# say_hello('Whats up')

# def say_hello(greeting):
#     name = input('Whats your name')
#     print(greeting, name)

# #MULTIPLES ARGUMENTS TO THE FUNCTION

# def say_hello(name, language):
#     if language == "HE":
#         print(f'Shalom, {name}')
#     elif language == "PT":
#         print(f'Ola, {name}')
#     elif language == "FR":
#         print(f'Bonjour, {name}')
#     else:
#         print(f'{language} is not supported')

# say_hello('Arielle','FR')
# #KEYWORDS ARGUMENTS
# say_hello(language = 'PT', name = 'Jonathan')

# #MULTIPLES ARGUMENTS TO THE FUNCTION WITH DEFAULT VALUES

# def say_hello(name, language = 'HE'):
#     if language == "HE":
#         print(f'Shalom, {name}')
#     elif language == "PT":
#         print(f'Ola, {name}')
#     elif language == "FR":
#         print(f'Bonjour, {name}')
#     else:
#         print(f'{language} is not supported')
# say_hello(name = 'Jonathan') #OUTPUT will also print 'HE' since it is default in the function

# #LOCAL vs GLOBAL SCOPE
# def say_hello(greeting):
#     name = input('Whats your name')
#     print(greeting, name)
# print(name) #in the global scope 'name' is not defined

# global_var = 100
# def calculation(a,b):
#     addition = a+b
#     substraction = a-b
#     global_var += addition #it is not highlighted since it is out of the scope of the function. To fix you need to add it as an argument or use the word variable 'global' inside the function
#     print(f{'addition = {addition}\n substraction = {substraction}'})
# calculation(5,7)


# def calculation(a,b):
#     global global_var
#     addition = a+b
#     substraction = a-b
#     global_var += addition #it is highlighted since it is been called. using 'global' 
#     print(f{'addition = {addition}\n substraction = {substraction}'})
# calculation(5,7)


#RETURNING VALUES
def calculation(a,b):
    addition = a+b
    substraction = a-b
    print(f'addition = {addition}') 
    return (addition, substraction)

addition, substraction = calculation(5,7)
total_value = 10

def increase_total(addition, total_value, substraction):
    result1 = total_value + addition
    result2 = total_value - substraction
    return (result1, result2) 
print(increase_total(addition, total_value, substraction)) #to see the function you need to print

students = ['Leah', 'Luke', 'Darth Vader']

def welcome(students):
    for name in students:
        print(f'Welcome {name}')

welcome(students)


def my_pets(*args):
    total_pets = len(args)
    return total_pets

print(my_pets('cat','dog','bird'))

def user_info(**kwargs): #for arguments for dictionaries
    print(kwargs) 

user_info(name = 'Jonathan', address = 'Ramat Gan', email = 'jo@gmail.com')

