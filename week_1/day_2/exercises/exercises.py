# ------ Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dec = zip(keys , values)
print (list(dec))
# ------ Exercise 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
family = {}
while True:
    name = input("Enter a family member's name or (done) to finish : ")
    if name.lower() == 'done':
        break
    age = int(input(f"Enter {name} age: "))
    family[name] = age

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"{name} has to pay: {price}$")
    total_cost += price

print(f"Total cost : {total_cost}$")

# ------ Exercise 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(brand["international_competitors"][-1])
print( brand["major_color"]["US"])
print( len(brand))
print( brand.keys())
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)
print( brand["number_stores"])

# ------ Exercise 4
def describe_city(city, country="morocco"):
    print(f'{city} is in {country}')
describe_city("rabat" , "morocco")
# ------ Exercise 5
import random

def number(user_number):
    if not (1 <= user_number <= 100):
        print("Please enter a number between 1 and 100.")
        return
    random_number = random.randint(1, 100)  
    if user_number == random_number:
        print(f"Success! Both numbers are {user_number}.")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")
number(25)

# ------ Exercise 6
def make_shirt(size , text):
    print(f'The of the shirt is {size} and the text is {text}')
make_shirt("Large", "Hello World")

def make_shirt(size= "Large", text="I love Python” by default"):
      print(f'The of the shirt is {size} and the text is {text}')
make_shirt()
make_shirt("meduim")
make_shirt(size="Small", text="i love javascript")
make_shirt(text="Code is Life", size="Extra Large")

# ------ Exercise 7
import random
def get_random_temp():
     random_temp = random.randint(-10 , 40)
     return random_temp
get_random_temp()

def main ():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} 2 degrees Celsius")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 17 <= temp <= 23:
        print("Nice weather, enjoy your day!")
    elif 24 <= temp <= 32:
        print("It's warm, stay hydrated.")
    elif 33 <= temp <= 40:
        print("It's really hot! Avoid staying too long in the sun.")

""""""""""""""
def get_random_temp(season):
    if season.lower() == "winter":
        low, high = -10, 16
    elif season.lower() == "spring":
        low, high = 5, 23
    elif season.lower() == "summer":
        low, high = 16, 40
    elif season.lower() in ["autumn", "fall"]:
        low, high = 0, 23
    else:
        print("Unknown season! Defaulting to full range.")
        low, high = -10, 40
    
    return random.randint(low, high)

def main():
    season = input("Enter the season (summer, autumn, winter, spring): ")
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp}.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 17 <= temp <= 23:
        print("Nice weather, enjoy your day!")
    elif 24 <= temp <= 32:
        print("It's warm, stay hydrated.")
    elif 33 <= temp <= 40:
        print("It's really hot! Avoid staying too long in the sun.")


main()
##########

def get_season_from_month(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"

def get_random_temp(season):
    if season == "winter":
        low, high = -10, 16
    elif season == "spring":
        low, high = 5, 23
    elif season == "summer":
        low, high = 16, 40
    elif season == "autumn":
        low, high = 0, 23
    else:
        low, high = -10, 40
    
    return round(random.uniform(low, high), 1)

def main():
    month = int(input("Enter the number of the month (1-12): "))
    season = get_season_from_month(month)
    
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} ({season}).")
    
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 17 <= temp <= 23:
        print("Nice weather, enjoy your day!")
    elif 24 <= temp <= 32:
        print("It's warm, stay hydrated.")
    elif 33 <= temp <= 40:
        print("It's really hot! Avoid staying too long in the sun.")

main()


# ------ Exercise 8

def ask_questions():
    questions = {
        "What is the capital of France? ": "paris",
        "What is 5 + 7? ": "12",
        "Who wrote 'Harry Potter'? ": "j.k. rowling",
        "What is the color of the sky on a clear day? ": "blue",
        "What is 10 * 2? ": "20"
    }
    
    correct_count = 0
    incorrect_count = 0
    wrong_answers = []
    
    for question, correct_answer in questions.items():
        user_answer = input(question).strip().lower()
        if user_answer == correct_answer.lower():
            correct_count += 1
        else:
            incorrect_count += 1
            wrong_answers.append((question, user_answer, correct_answer))
    
    return correct_count, incorrect_count, wrong_answers


def show_results(correct, incorrect, wrong_answers):
    print(f"\n Correct answers: {correct}")
    print(f" Incorrect answers: {incorrect}")
    
    if wrong_answers:
        print("\n--- Wrong Answers ---")
        for q, user_ans, correct_ans in wrong_answers:
            print(f"Q: {q}")
            print(f"   Your answer: {user_ans}")
            print(f"   Correct answer: {correct_ans}")
    
    if incorrect > 3:
        print("\nYou had more than 3 wrong answers. Let's try again!\n")
        main()


def main():
    correct, incorrect, wrong_answers = ask_questions()
    show_results(correct, incorrect, wrong_answers)

main()
