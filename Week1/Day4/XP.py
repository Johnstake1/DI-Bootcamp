# #EX1

def display_message():
    print('I am learning Python')
display_message()

# #EX2

def favourite_book(title):
    print(f'One of my favorite books is {title}')
favourite_book('Alice in Wonderland')

# #EX3

def describe_city(city, country):
    print(f'{city} is in {country}')

describe_city('TLV', 'Israel')


def describe_city(city, country = 'Argentina'):
    print(f'{city} is in {country}')

describe_city(city ='Buenos Aires')

# #EX4
import random

def random_num(num):
   random_num = random.randint(1,101)
   print(random_num)
   if random_num == num:
       print('Success')
   else:
       print('try again') 

random_num(44)

# #EX5
def make_shirt(size, text):
    print(f'The size of the shirt is {size} and the text is {text}')
make_shirt('40', 'This is frustrating')

#EX5.4

def make_shirt(size = 'Large', text = 'I Love Python'):
    print(f'The size of the shirt is {size} and the text is {text}')
make_shirt()
make_shirt(size = 'Medium')
make_shirt(size = 'Small', text = 'Vamos Argentina')

#BONUS

def make_shirts(**kwargs):
    for size, text in kwargs.items():
            print(f'The size of the shirt is {size} and the text is {text}')

make_shirts(size = 'small', text = 'Go Donald')

# #EX6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
      for magicians in magician_names:
            print(f'{magicians}')

show_magicians()

def make_great():
      for magicians in magician_names:
            magicians.

# #EX7.1
import random

def get_random_temp():
      temperature = random.randint(-11,40)
      print(temperature)
      return (temperature)

get_random_temp()
# #EX7.2 and 7.3
def main():
    stored_temperatue = get_random_temp()
    print(f'The temperature is {stored_temperatue} degrees Celsius')
    if stored_temperatue < 0:
          print('Brrr, that’s freezing! Wear some extra layers today')
    elif stored_temperatue < 16:
          print('Quite chilly! Don’t forget your coat')
    elif stored_temperatue <23:
          print('Wear a tshirt')
    elif stored_temperatue <32:
          print('Looks like someone is going to the beach')
    elif stored_temperatue <40:
          print('This is too hot')
    
main()

# #EX7.4.1 & 7.4.2
import random
def get_random_temp2():
      winter_t = random.randint(-11,10)
      autumn_t = random.randint(11,18)
      spring_t = random.randint(19,25)
      summer_t = random.randint(26,40)
      print(f'Winter temperature = {winter_t}\n Autumn temperature = {autumn_t}\n Spring temperature = {spring_t}\n Summer temperature = {summer_t}')
      return {'winter' : winter_t, 
                  'autumn' : autumn_t, 
                  'spring' : spring_t, 
                  'summer' : summer_t}

# #EX7.4.3
def main2():
    answer = input('What is your favorite season\n')
    stored_temperature = get_random_temp2()
    if answer in stored_temperature:
          print(f'The temperature in {answer} is {stored_temperature[answer]}')

#EX8 - #my brain is dead...sorry!
    
