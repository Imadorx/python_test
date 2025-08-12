# ------ Exercise 1

text = range(1,5)
for i in text:
    print("hello world")

# ------ Exercise 2

resulte = (99 **3 )*8
print (resulte)

# ------ Exercise 3

UserName = input("give me your name : ")
if UserName == "imad" : 
   print ("you are my brother")
else:
   print ("your are not my brother")

# ------ Exercise 4

height =int (input("enter your height in cm : "))
if height >= 145 :
 print("you are tall enough to ride")
else:
 print("You need to grow some more to ride")

# ------ Exercise 5

my_fav_numbers = set()
my_fav_numbers = {777 , 444 ,111}
print(my_fav_numbers)
my_fav_numbers.add(555)
my_fav_numbers.add(999)
print(my_fav_numbers)
my_fav_numbers.remove(444)
print(my_fav_numbers)
friend_fav_numbers =set()
friend_fav_numbers ={777 , 222 , 888}
print(friend_fav_numbers)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# ------ Exercise 6

# non 


# ------ Exercise 7

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove('Banana')
print(basket)
basket.remove('Blueberries')
print(basket)
basket.append('Kiwi')
print(basket)
basket.insert(1 ,' Apples')
print(basket)
basket.count("Apples")
print(basket)
basket.clear()
print(basket)

# ------ Exercise 8

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in    sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    print( sandwich_orders)

finished_sandwiches = []

 
while  sandwich_orders :
  sandwich=  sandwich_orders.pop(0)
    # print(sandwich_orders)
finished_sandwiches.append(sandwich)
print(finished_sandwiches)

