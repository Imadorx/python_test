# ------ Exercise 1
birthdays = {
    "imad": "1995/07/12",
    "mehdi": "1988/03/25",
    "fati": "2000/12/05",
    "sami": "1992/11/20",
    "marwa": "1999/01/15"
}

print(" Welcome to the Birthday Dictionary")
print("You can look up the birthdays of the people in the list")

person = input("\nEnter a name to find their birthday: ").strip()

if person in birthdays:
    print(f"\n {person}'s birthday is on {birthdays[person]}")
else:
    print("\n Sorry, we don't have that person's birthday in the list.")

# ------ Exercise 2
birthdays = {
    "imad": "1995/07/12",
    "mehdi": "1988/03/25",
    "fati": "2000/12/05",
    "sami": "1992/11/20",
    "marwa": "1999/01/15"
}

print(" Welcome to the Birthday Dictionary")
print("You can look up the birthdays of the people in the list")

print("\nWe have birthdays for:")
for name in birthdays:
    print(f" - {name}")

person = input("\nEnter a name to find their birthday: ").strip()

if person in birthdays:
    print(f"\n {person}'s birthday is on {birthdays[person]}")
else:
    print("\n Sorry, we don't have that person's birthday in the list.")
# ------ Exercise 3

def calculate_pattern_sum(x):
    x_str = str(x)
    
    num1 = int(x_str)
    num2 = int(x_str * 2)
    num3 = int(x_str * 3)
    num4 = int(x_str * 4)
    
    total = num1 + num2 + num3 + num4
    return total
print(result = calculate_pattern_sum(3))
  

# ------ Exercise 4
import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1
        if dice1 == dice2:
            break
    return count

def main():
    results = []       
    for _ in range(100):
        throws_needed = throw_until_doubles()
        results.append(throws_needed)
    
    total_throws = sum(results)
    average_throws = total_throws / len(results)
    
    print(f" Total throws: {total_throws}")
    print(f" Average throws to reach doubles: {average_throws:.2f}")

main()