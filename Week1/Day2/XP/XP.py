# #EX1 Favorite Numbers

# my_fav_numbers = {1,2,3,8,7}
# my_fav_numbers.add(10)
# my_fav_numbers.add(20)
# my_fav_numbers.remove(20)

# friend_fav_numbers = {7,8,10,68,100,47}
# our_fav_numbers = my_fav_numbers.intersection(friend_fav_numbers)
# print(my_fav_numbers)
# print(friend_fav_numbers)
# print(our_fav_numbers)

# #EX2 Tuple

# #By defition NO, yet there are workarounds on how to bypass the tuples' attributes.

# #EX3 List

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove('Banana')
# basket.remove('Blueberries')
# print(basket)
# basket.append('Kiwi')
# basket.insert(0,'Apples')

# print(basket)
# basket.count('Apples')
# print(basket.count('Apples'))
# basket.clear()
# print(basket)

# #EX4 Floats

# # An integer is a whole number, whereas floats are decimal numbers.
# #1

# sequence = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# print(sequence)
# print(type(sequence))
# #2 - FOR CHECKER: you can always use the built in method, but I try to use the iteration to make it more interesting.
# stored_values = []
# keep_asking = True
# while keep_asking:
#     input_sequence = input('Write a sequence of numbers. Press q to finish')
#     if input_sequence == 'q':
#         keep_asking = False
#     else:
#         stored_values.append(input_sequence)
# print(stored_values)

# #EX5 For Loop
# List = []
# for i in range(1,21):
#     print(i)
#     List.append(i)
# print(List)

# for i in enumerate(List):
#     print(i)

# #EX6 While Lopp

# names = []
# keep_asking = True
# while keep_asking:
#     your_name = input('Write your name. Press Q to finish')
#     if your_name == 'Jonathan':
#         keep_asking = False
#     else:
#         names.append(your_name)
# print(names)

#EX7 Favorite Fruits

# fruits = []
# keep_asking = True
# while keep_asking:
#     question = input('What are your favorite fruits? (Write each fruit with a single space. Close with q')
#     if question == 'q':
#         keep_asking = False
#     else:
#         fruits = question.split()
# print(fruits)


# ask_input = input('Write a fruit')
# if ask_input in fruits:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
#     print('You chose a new fruit. I hope you enjoy')

#EX8

# pizza_topping = []
# keep_asking = True
# while keep_asking:
#     question = input('What toppings do you want with your pizza? Close with quit')
#     if question == 'quit':
#         keep_asking = False
#     elif question != 'quit':
#         pizza_topping.append(question)
#         print('Adding your topping')
# count_topings = len(pizza_topping)
# price_per_topping = 2.5
# pizza_price = 10

# print(f'Your total price is {pizza_price} + {price_per_topping*count_topings}')

#EX9
#FOR CHECKER - I got Stucked here
# family =[]
# keep_asking = True

# while keep_asking:
#     question = input('What is your age?')
#     if question == 'q':
#         keep_asking = False
#     elif question !='q':
#         family.append(question)


# ticket_price = 0
# new_family = int(family)
# for age in new_family:
#     if age < 3:
#         ticket_price = 0
#     elif 3 <= age >= 12:
#         ticket_price = 10
#     else:
#         ticket_price = 25
# print(ticket_price)

#EX10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# Removing all "Pastrami sandwich" from the list
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# Preparing the sandwiches
finished_sandwiches = []

# Loop through the remaining orders
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print("I made your " + sandwich)

    

