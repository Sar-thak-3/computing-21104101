print("******************************QUESTION 1********************************")
string = "Python is a case sensitive language"
print("The length of entered string(including spaces) is ",len(string))

# Convert string to list with words as different list items
list_ = string.split()
# Reverse the list items
reverse_list = list_[::-1]
str1 = " "
# Joining the list items into the string
print(str1.join(reverse_list))

#c) Slicing to produce new_string
new_string = string[10:26]
print(new_string)

#d) Replacing "a case sensitive" with "object oriented"
new_string = "object oriented"
print(new_string)

#e) Index of string "a" in string
print(string.index('a'))
 
#f) Remove spaces from string
print(string.replace(" ", ""))

print("******************************QUESTION 2*********************************")
name = "SARTHAK GARG"                     # String
department = ("Electrical engineering",)  # Tuple
sid = 21104101                            # Int
cgpa = 9.9                                # Float
print(f"Hey {name!r} here!")
print(f"My SID is {sid}")
print(f"I am from {department[0]} and my cgpa is {cgpa}")

print("******************************QUESTION 3*********************************")
a = 56 ; b = 10
print("Bitwise AND:",a&b)
print("Bitwise OR",a|b)
print("Bitwise XOR",a^b)
print("Left shift a by 2 bits:",a>>2," ,Left shift b by 2 bits:",b>>2)
print("Right shift a by 2 bits:",a<<2," ,Right shift b by 4 bits:",b<<4)

print("******************************QUESTION 4*********************************")
num1 = (input("Enter 1st number: "))
num2 = (input("Enter 2nd number: "))
num3 = (input("Enter 3rd number: "))

if num1>num2:
    if num1>num3:
        print(num1+" is greatest number.")
else:
    if num2>num3:
        print(num2+" is greatest number.")         
    else:
        print(num3+" is greatest number.")

print("******************************QUESTION 5*********************************")
string = input("Enter the string , introducing yourself!: ")
if 'name' in string.lower():
    print("YES")
else:
    print("NO")

print("******************************QUESTION 6*********************************")
side1 = float(input("Enter the length of 1st side: "))
side2 = float(input("Enter the length of 2nd side: "))
side3 = float(input("Enter the length of 3rd side: "))
side1=int(side1)
side2=int(side2)
side3=int(side3)
# # Triangle is formed only when sum of any 2 sides of traingle is greater than 3rd side.
# # As mentioned in question so converted to integer and then condition is checked.
if ((side1)+(side2))>((side3)) and ((side2)+(side3))>((side1)) and ((side1)+(side3))>((side2)):
    print("YES")
else:
    print("NO")