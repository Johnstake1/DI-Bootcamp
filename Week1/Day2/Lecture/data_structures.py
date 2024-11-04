#List, Iterating and Formatting Data
#Containers for values such as boolean; strings; float; integers; etc
#DATA STRUCTURES:
# sequences = string
# data structure sequence: list
# sets
# tuples

my_name = 'Jonathan'
last_name = 'Svetskin'
user_name = 'jsvetskin'

# Two options to create a list
user_info = [my_name, last_name, user_name] #wrap with square brakets
user_name = list(my_name) #use built in method list()

print(user_info)
print(user_name)

nums_list = [1,2,4,7,2,8,12]

#methods for list
nums_list.append(120) #Adds to the last one
print(nums_list)

nums_list.insert(2, 55) #Adds to a specific index
print(nums_list)

nums_list.remove(2) #remove first appearance of an element in the list
print(nums_list)
del nums_list[3] #removes/delete the index position
print(nums_list) 
nums_list.pop() # delete last element and saves what was deleted
nums_list.pop(3)
print(nums_list)

deleted_element = nums_list.pop(3)
print(deleted_element)

print(nums_list[3])

some_tuple = tuple()
scores = (10,45,33,67)

#unpack a tuple
score1, score2, score3, score4 =scores

print(score1)
print(score2)
print(score3)

# A workaround on how to change tuple to list and back to tuples
scores_list = list(scores) 
scores_list.append(120)
updated_tuple = tuple(scores_list) 
print(scores)
print(updated_tuple)

#Example - 
list1 = [5, 10, 15, 20, 25, 50, 20]
list1.remove(20)
list1.insert(3, 200)
print(list1)

#Best way to do it
if list1.index(20):
    list1[list1.index(20)] = 200


#SETS: Unordered and doesn't accept multiple occurrences. It is impossible to index.

#my_set = {''}
my_set = set()

my_set.add('Rick')
my_set.add('Morty')
my_set.add('Rick')
print(my_set)

set2 = {'Harry', 'Ron', 'Morty'}
set3 = my_set.intersection(set2)
print(set3)

set4 = my_set.union(set2)
print(set4)

names = ['Leah', 'Luke', 'Chubaka', 'Harry', 'Harry']
names_set = set(names)
print(names_set)

names = list(names_set)
print(names) #It does not have Harry repeated.



