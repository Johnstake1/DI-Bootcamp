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
                             

# print(user_info_dict['name'])
# print(user_info_dict['pets'][1])
# print(user_info_dict['family']['relation'])
# print(user_info_dict['hobbies'][2][1])

#FOR LOOPS IN DICTIONARIES

# for key in user_info_dict.keys():
#     print(key) #prints the names of the keys. Very usefull for user information dictonaries and look for data

# for value in user_info_dict.values():
#     print(value)

# for key,value in user_info_dict.items():
#     print(f'key:{key}')
#     print(f'value: {value}')

# #CHANGE VALUES IN KEYS

# user_info_dict['email'] = 'svet@gmail.com'

# #ADDING KEYS & VALUES

# user_info_dict['profession'] = 'Finance'

# user_info_dict.update({'address': 'Ramat Gan'})


# #DELETE A KEY VALUE PAIR (an entry) of the dict

# del user_info_dict['profession']

#CHECKING IF A KEY/VALUE EXISTS IN THE DICT

# print('pets' in user_info_dict.keys())
# print('Jonathan' in user_info_dict.values())

# print(user_info_dict)

#UPDATE() --> MERGES DICTIONARIES OR UPDATES AND ENTRY

user_info_dict['family'].append({'name': 'Daniel',
                                 'age': 36,
                                 'relation': 'brother'})


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


