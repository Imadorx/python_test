from datetime import datetime

def is_leap_year(year):
    """Check if a year is a leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")

today = datetime.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

candles = age % 10
if candles == 0:  
    candles = 10

cake_top = "       " + "i" * candles
cake = f"""
{cake_top}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""


if is_leap_year(birthdate.year):
    print("Leap year baby! You get 2 cakes!")
    print(cake * 2)
else:
    print(cake)
