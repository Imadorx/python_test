# ------ Challenge 1

number = int (input("gave your number : "))
lenght = int (input("gave your lenght : "))
 
my_list =[]
for i in range (1, lenght +1) : 
    my_list.append(number*i)
print(my_list)

# ------ Challenge 2
str=input("entrer un string")
newStr=""
for i in range (len(str)):
   if i == len(str) - 1 or str[i] != str[i + 1]:
        newStr+=str[i]
print(f"{newStr}")



