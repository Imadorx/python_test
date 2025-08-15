# ------ Exercise 1
cars_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

cars_list = [car.strip() for car in cars_str.split(",")]

print(f"Number of manufacturers: {len(cars_list)}")

cars_list_sorted = sorted(cars_list, reverse=True)
print("Manufacturers in reverse order (Z-A):")
print(cars_list_sorted)

count_o = sum(1 for car in cars_list if 'o' in car.lower())
print(f"Number of manufacturers with 'o': {count_o}")

count_no_i = sum(1 for car in cars_list if 'i' not in car.lower())
print(f"Number of manufacturers without 'i': {count_no_i}")

companies = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

unique_companies = list(set(companies))

companies_str = ", ".join(unique_companies)
print(f"Companies without duplicates ({len(unique_companies)} total):")
print(companies_str)

reversed_sorted_companies = sorted([company[::-1] for company in unique_companies])
print("\nBonus - Reversed names in ascending order (A-Z):")
print(", ".join(reversed_sorted_companies))


# ------ Exercise 2
def get_full_name(first_name, last_name, middle_name=""):
   
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

print(get_full_name(first_name="imad", middle_name="eddine", last_name="kaaouane"))  
print(get_full_name(first_name="ibrahim", last_name="boutar"))                        

# ------ Exercise 3
english_to_morse = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/"  
}

morse_to_english = {value: key for key, value in english_to_morse.items()}

def english_to_morse_func(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in english_to_morse:
            morse_code.append(english_to_morse[char])
    return " ".join(morse_code)

def morse_to_english_func(morse_text):
    words = morse_text.split(" / ")  
    decoded_words = []
    for word in words:
        letters = word.split()    
        decoded_word = "".join(morse_to_english.get(letter, "") for letter in letters)
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)


text = "Hello World"
morse = english_to_morse_func(text)
print(f"English: {text}")
print(f"Morse: {morse}")

decoded = morse_to_english_func(morse)
print(f"Decoded back: {decoded}")
