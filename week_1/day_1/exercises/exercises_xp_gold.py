# ------ Exercise 1
month = int(input("Enter a month number : "))

if month in (3, 4, 5):
    print("Spring")
elif month in (6, 7, 8):
    print("Summer")
elif month in (9, 10, 11):
    print("Autumn")
elif month in (12, 1, 2):
    print("Winter")

# ------ Exercise 2

for i in range(1, 21):
    print (i)
numbers = list (range(1,21))
print (numbers)
for x in range (len(numbers)):
    if x % 2 == 0:
     print(numbers[x])

# ------ Exercise 3

while True:
    user_name = input("Enter your name: ")
    if user_name == "imad":
        print("That's my name.")
        break

# ------ Exercise 4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter a name: ")

if user_name in names:
    print(f"{user_name} found at index {names.index(user_name)}")
else:
    print(f"{user_name} not found in the list.")

# ------ Exercise 5
num_1 = input("entre the 1st numbe: ")
num_2 = input("entre the 2st numbe: ")
num_3 = input("entre the 3st numbe: ")

greatest = max(num_1, num_2, num_3)
print(f"The greatest number is: {greatest}")

# ------ Exercise 6

import random

wins = 0
losses = 0

while True:
    guess = input("Guess a number between 1 and 9 (or 'quit' to exit): ")
    if guess.lower() == 'quit':
        break

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    if guess < 1 or guess > 9:
        print("Number out of range.")
        continue

    random_num = random.randint(1, 9)
    print(f"The random number was: {random_num}")

    if guess == random_num:
        print("Winner!")
        wins += 1
    else:
        print("Better luck next time.")
        losses += 1

print(f"Game over. Wins: {wins}, Losses: {losses}")


