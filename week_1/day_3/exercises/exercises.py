# ------ Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

   
   
cat_1 = Cat("macha ", 1 )
cat_2 = Cat("lili ", 3 )
cat_3 = Cat("miro ", 2 )


def cat_older(*cats):
    return max(cats, key=lambda cat: cat.age)

oldest = cat_older(cat_1, cat_2, cat_3)
print(f"The oldest cat in this list is {oldest.name} and he is {oldest.age} years old.")

# ------ Exercise 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")



davids_dog = Dog("Rex", 50)
print(f"David's dog is named {davids_dog.name} and his height is {davids_dog.height} cm.")
davids_dog.bark()
davids_dog.jump()




sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog is named {sarahs_dog.name} and his height is {sarahs_dog.height} cm.")
sarahs_dog.bark()
sarahs_dog.jump()



if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
elif davids_dog.height < sarahs_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}.")
else:
    print("Both dogs are the same height!")

# ------ Exercise 3

class Songs ():
    def __init__ (self , lyrics):
        self.lyrics= lyrics
    def sing_me_a_song(self):    
        for line in self.lyrics:
          print(line)
stairway= Songs(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven "])      
stairway.sing_me_a_song()
# ------ Exercise 4
class Zoo:
    def __init__(self, zoo_name):
      
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
      
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(f"Animals in {self.name} Zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
   
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):

        sorted_animals = sorted(self.animals)
        grouped = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(animal)

        self.animal_groups = grouped

    def get_groups(self):
        print(f"Animal groups in {self.name} Zoo:")
        for letter, group in self.animal_groups.items():
            print(f"{letter}: {group}")
# ------ Exercise 5


