# DIFFERENCES BTW LISTS AND DICTIONARIES

fruits =['banana', 'apple', 'kiwi']
print(fruits[1]) #with lists we can access the data inside by index

user_info = ['Jonathan', 'jo@gmail.com', 35, True, 1.72]

user_info_dict = {'name': 'Jonathan',
                  'email': 'jo@gmail.com',
                  'age': 34,
                  'is male': True,
                  'height' : 1.72,
                  'pets': ['Caramelo', 'Paco', 'Ringo'],
                  'family': [{'name': 'Ariel',
                              'age': 5,
                             'relation':'son'}],
                             'hobbies' : [('Yoga', 3),('tennis', 1), ('chess', 3)]}
                             

print(user_info_dict['name'])
print(user_info_dict['pets'][1])
print(user_info_dict['family']['relation'])
print(user_info_dict['hobbies'][2][1])

#FOR LOOPS IN DICTIONARIES

for key in user_info_dict.keys():
    print(key) #prints the names of the keys. Very usefull for user information dictonaries and look for data

for value in user_info_dict.values():
    print(value)

for key,value in user_info_dict.items():
    print(f'key:{key}')
    print(f'value: {value}')

#CHANGE VALUES IN KEYS

user_info_dict['email'] = 'svet@gmail.com'

#ADDING KEYS & VALUES

user_info_dict['profession'] = 'Finance'

user_info_dict.update({'address': 'Ramat Gan'})


#DELETE A KEY VALUE PAIR (an entry) of the dict

del user_info_dict['profession']

#CHECKING IF A KEY/VALUE EXISTS IN THE DICT

print('pets' in user_info_dict.keys())
print('Jonathan' in user_info_dict.values())

print(user_info_dict)

#UPDATE() --> MERGES DICTIONARIES OR UPDATES AND ENTRY

user_info_dict['family'].append({'name': 'Daniel',
                                 'age': 36,
                                 'relation': 'brother'})

user_info2 = {}

user_info_dict.update(user_info2)


#Example:

# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sample_dict['class']['student']['marks']['history'])

# user_name = input('whats your name? ')
# user_email = input('your email')

# user_dict = {'Name:': user_name,
#              'email': user_email
#              }

#You can create keys from variables
#user_dict = {user_name: user_name,
#              'email': user_email
#             }

#CLASS EXERCISE: Delete set of keys from the dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

even_numbers = []

for i in range(1,20):
    if i%2 ==0:
        even_numbers.append(i)

print(even_numbers)

#ENUMARETE creates tuples where the (index, values)
students = ['John', 'Anna','Cathe', 'Mark']
for index, name in enumerate(students):
    print(index,name)

#ZIP
list1 = ['a', 'b', 'c']
list2 = [1,2,3]
list3 = list(zip(list1,list2)) #Outcome is tuple within a list

print(list3)

#BREAK, CONTINUE, PASS
#BREAK = STOP
#CONTINUE = DO NOTHING
#PASS = SIMILAR TO CONTINUE

#WHILE TRUE

total_family = []

while True:
    family_member = input('give me first age, type "quit" to exit')
    if family_member == 'quit':
        break
    total_family.append(family_member)
print(total_family)    

#CONTINUE: The loop will continue to the next iteration

for each_student in students:
    print(f'{each_student}, how are you? ')
    if each_student == 'Cathe':
        continue
    else:
        print('Hola')

#PASS:

if students[0] is 'Hello Harry':
    pass #a developer keyword to help the code before you have the logic
else:
    print('Not Harry')

#List Comprehension (FOR APPENDING ONLY)

even_nums = [i for i in range(1,20) if i%2 == 0]
print(even_nums)

#DICT COMPREHENSION

family_age = {'Lea': 12,
              'Mark': 25,
              'George' : 50}

new_year = 1

new_family_age = {name:age + 1 for (name,age) in family_age.items()}
print(new_family_age)
