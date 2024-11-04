#LOOPS - iterations over a certain sequence until a certain condition is met.
#FOR LOOPS

#syntax

students = ['Alex', 'Noa', 'Sara', 'Dima']

for each_student in students:
    if each_student == 'Dima':
        print(f'Doble Ultra, {each_student}')
    else:
        print(f'Good Morning, {each_student}')


for i in range(1,10):
    print('Hello there')

for i in range(len(students)):
    print(f'Hello there {i}')

for i, each_student in enumerate(students):
    print(i, each_student)

my_nums = [3,5,7,8,10]

print(max(my_nums))
print(min(my_nums))
print(sum(my_nums))

output = 0
for i in range(len(my_nums)):
    output += my_nums[i]
print(output)

#WHILE LOOPS
i = 0
while i < 10:
    print(f'Hi {i}')
    i += 1

family = []
members = input('Write the family member name. Press Q to finish')

while members != 'q':
    members = input('Write the family member name. Press Q to finish')
    family.append(members)
  
print(family)


#another way of doing it is using a FLAG
family = [[]]
keep_asking = True
while keep_asking:
    members = input('Write the family member name. Press Q to finish')
    if members == 'q':
        keep_asking = False
    else:
        family.append(members)
print(family)
            