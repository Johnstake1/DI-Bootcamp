#EX1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

my_cat = Cat('Miguel', 14)
adopted_cat = Cat('Ricardo', 2)
friend_cat = Cat('Manuel', 4)
print(f'My cats name is {my_cat.name}, he is {my_cat.age}')
print(f'We adopted a cat, his name is {adopted_cat.name}. He is {adopted_cat.age} years old')
print(f'My friend has a cat. His name is {friend_cat.name}. He is {friend_cat.age} years old')

my_cats = [my_cat, adopted_cat, friend_cat]

def oldest_cat():
    old_cat=0
    for cat in my_cats:
        if old_cat < cat.age:
           old_cat = cat    
        return old_cat
print(oldest_cat())
old_cat = oldest_cat()
print(old_cat.name)
print(old_cat.age)

#EX2

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        return(f'{self.name} goes woof')
    
    def jump(self,name,height):
        self.name = name
        self.height = height *2
        return(f'{self.name} jumps {self.height}')

davids_dog = Dog('Rex', 50)
print(davids_dog.name)
print(davids_dog.height)

print(davids_dog.bark())
print(davids_dog.jump('Rex', 50))

sarahs_dog = Dog('Teacup', 20)
print(sarahs_dog.name)
print(sarahs_dog.height)
print(sarahs_dog.bark())
print(sarahs_dog.jump('Teacup', 20))

# their_dogs = [davids_dog, sarahs_dog]
# def oldest_dog():
#     old_dog=0
#     for dog in their_dogs:
#         if dog <= dog.height:
#            dog = old_dog    
#         return old_dog
# print(oldest_dog())

#EX3

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        print(self.lyrics)
        
stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

#EX4
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self,*args):
        for arg in args:
            self.animals.append(arg)
        self.animals = sorted(self.animals)
        print(self.animals)
        return self.animals
    
    def get_animal(self):
        print(self.animals)

    def sell_animals(self, animal_sold):
        for animal in self.animals:
             if animal == animal_sold:
                 self.animals.remove(animal)
        print(self.animals)
        return(self.animals)

    def sort_animals(self):          
        self.sorted_animals = {}
        for i, animal in enumerate(self.animals):
            if i+1 <= len(self.animals):
                if animal[0] == self.animals[i+1][0]:
                        self.sorted_animals[i+1] = self.animals.append(animal)
            else:      
                print(self.sorted_animals)
                return self.sorted_animals
    

        
    def get_groups(self):
        for group in self.sorted_animals.values():
            print(group)

ramat_gan_safari = Zoo('Ramat Gan')
ramat_gan_safari.add_animal('Dolphin', 'Cat', 'Tiger', 'Lion')
ramat_gan_safari.get_animal()
ramat_gan_safari.sell_animals('Cat')
ramat_gan_safari.sort_animals()
ramat_gan_safari.add_animal('Ape', 'Dog', 'Crocodile', 'Leopard')
print(ramat_gan_safari.animals)
ramat_gan_safari.sort_animals()


