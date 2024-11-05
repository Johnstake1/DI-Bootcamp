# #EX1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# print(dict(zip(keys,values)))

# #EX2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# total_price = 0
# for key, value in family.items():
#     if int(value) < 3:
#         total_price = 0
#         print(f'{key} has to pay 0' )
#     elif int(value) <=12:
#         total_price +=10
#         print(f'{key} has to pay 10')
#     else:
#         total_price +=15
#         print(f'{key} has to pay 15')
# print(f'The total price to pay is {total_price}')

# #EX2.5

# family = {}

# question = input('What is your name?')
# question2 = input('What is your age?')

#EX3
# brand = {'name':'Zara',
#          'creation_date': 1795,
#          'creator_name': 'Amancio Ortega Gaona',
#          'type of clothes': ['men', 'women', 'children','home'],
#          'international competitors' : ['Gap', 'H&M', 'Benetton'],
#          'number of stores': 7000,
#          'major_color': {'France': 'blue',
#                          'Spain':'red',
#                          'US':['pink','green']}}
# brand['number of stores'] = 2

# brand['country_creation'] = 'Spain'
# brand['international competitors'] = 'Desigual'
# del brand['creation_date']

# print('The last added international competitor is' )
# print(f'The major clother colors in the US are ')

# more_on_zara = {'creation_date': 1975 ,
#             'number_stores': 10000}
# brand.update(more_on_zara)
# print(brand['number of stores'])

#EX4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {}
disney_users_B = {}
disney_users_C = {}
for i in range(5):
    disney_users_A[users[i]] = i

print(disney_users_A)

for i, users in zip(range(5), users):
    disney_users_B[i] = users

print(disney_users_B)

new_users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

sorted_users = sorted(new_users)

for i in range(5):
    disney_users_C[new_users[i]] = i
print(disney_users_C)


