#EX1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):    
    def sing(self, sounds):
        return f'{sounds}'

cat1 = Bengal('Fluffy', 4)
cat2 = Chartreux('Vanilla', 8)
cat3 = Siamese('Marcos', 2)

all_cats = [cat1,cat2,cat3]

sara_pets = Pets(all_cats)

sara_pets.walk()

#EX2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print(f'{self.name} is barking')
    def run_speed(self):
        print((self.weight/self.age)*10)
        return (self.weight/self.age)*10
    def fight(self, other_dog):
        d_speed = self.run_speed()
        d_weight_speed = d_speed * self.weight
        od_speed = other_dog.run_speed()
        od_weight_speed = od_speed * other_dog.weight
        if d_weight_speed > od_weight_speed:
            print(f'{self.name} wins')
        else:
            print(f'{other_dog.name} wins')

other_dog = Dog('Rex', 10, 40)
dog1 = Dog('Ringo', 12, 45)

other_dog.run_speed()
dog1.run_speed()

dog1.fight(other_dog)
other_dog.fight(dog1)

# #EX3

# in dog.py file



# #EX4 #FOR CHECKER: I got frustrated when approaching the creationg of the dictionary :/
class Family():

    def member(self, members, last_name):
        self.members = []
        self.last_name = last_name

    def born(self, **kwargs):
        self.new_born = {}
        self.members.append(self.new_born)
        print('Congratulations')
    def is_18(self, member):
        if self.members > 18:
            return True
        else:
            return False
    def family_presentation(last_name, members):
        
baby1 = Family()
baby1.born(1, 'Maria')

# #EX5 # I understand that I cannot do EX5 without completing EX4...

# class TheIncredibles(Family):



        