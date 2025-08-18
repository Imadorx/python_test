# ------ Exercise 1
import math
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def definition(self):
        print("A circle is the set of all points in a plane that are at a given distance (radius) from a fixed point (the center).") 

# ------ Exercise 2
import random
class List :
    def __init__(self, letter):
        self.letter=letter
    def reversed_list(self):
      return self.letter[::-1]
    def sorted (self):
       return sorted(self.letter)
    def random_list(self):
      return [random.randint(0, 100) for _ in range(len(self.letters))]
   
# ------ Exercise 3

# ------ Exercise 4

# ------ Exercise 5

# ------ Exercise 6

# ------ Exercise 7

# ------ Exercise 8
