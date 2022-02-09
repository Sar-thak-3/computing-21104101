print("****************************************QUESTION 1**************************************")

string = input("Enter the string: ").lower()
# Split the string from spaces to check either only one word or many words
listt = string.split()
new_string = ""
new_list = []
# If length of list we obtained through is 1 then we give occurences of each character otherwise of each word!
if len(listt)==1:
    for char in string:
        new_string = new_string + char
        if new_string.count(char)>1:
            continue
        else:
            print(char," repeated ",string.count(char),"times")

else:
    for item in listt:
        new_list.append(item)
        if new_list.count(item)>1:
            continue
        else:
            print(item," repeated ",listt.count(item),"times")

print("****************************************QUESTION 2**************************************") 

day = int(input("Enter the day: "))
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

def leap_year():
    # Checking leap year or not
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0) :
        return True

def year_check(year):
    # Checking either year comes in given range or not
    if year<=1800 or year>=2025:
        return False    

def month_check(month):
    # Giving days exist in month according to the months in year
    if month in [4,6,9,11]:
        days_exist = range(1,31)
    elif month in [1,3,5,7,8,10,12]:
        days_exist = range(1,32)    
    elif month==2:
        if leap_year() == True:
            days_exist = range(1,30)
        else:
            days_exist = range(1,29)
    else:
        # If any incorrect month entered return None
        return None
    return days_exist    

# IF month is incorrect or year is incorrect then print below statement 
if (month_check(month)==None) or (year_check(year)==False):
    print("No such date exist")
#If month year exist then processing the new date! 
elif day in month_check(month):
    day += 1
    if day in month_check(month):
        print("Next date is: ",day,month,year)
    else:
        day = 1
        month += 1
        if month == 13 and day == 1:
            year += 1 
            month = 1
        print("Next date is: ",day,month,year)    
# If day is incorrect print below statement. 
else:
    print("No such date exist")

print("****************************************QUESTION 3**************************************")

given_list = [3,9,10,15]
square_list = []

for num in given_list:
    # For each item in given_list we append square_list with square of each item
    square_list.append(num**2)

# Zipping item in given to corresponding item in square list
print(list(zip(given_list,square_list)))

print("****************************************QUESTION 4**************************************")

grade_point = int(input("Enter the grade points: "))
# Chart for (grade|performace|grade points) in form of dictionary
chart = {4:['D','Poor'] , 5:['C','Below average'] , 6:['C+','Average'] , 7:['B','Good'] , 8:['B+','Very Good'] , 9:['A','Excellent'] , 10:['A+','Outstanding']}

# If 4<grade points<10 , then show the performance and grade points of student. 
if grade_point>10 or grade_point<4:
    print("ERROR ,wrong grade entered!")
else:
    print(f"Your grade is {chart[grade_point][0]} and {chart[grade_point][1]} performance")

print("****************************************QUESTION 5**************************************")    

string = 'ABCDEFGHIJK'  
while(True):
    print(f"{string:^11}")
    # Popping last 2 character from string.
    string = string[:-2]
    # At last time the len of string remaining is 1 so when popped 2 character length remains is 0 
    if len(string)==0:
        break

print("****************************************QUESTION 6*************************************")

student_dict = {}
while(True):
    sid = int(input("Enter the 8 digit student id: "))
    name = input("Enter the name of the student: ")
    student_dict[sid] = name
    condition = input("All students done?: y-YES/n-NO ").lower()
    # Now if we enter 'yes' the loops break 
    if condition == "y":
        break

# a) Print student info containing dictionary
print(student_dict)

# b) Sort dictionary using names(MY OWN METHOD NOT EVEN COPIED FROM GOOGLE!)
sorted_values = sorted(student_dict.values()) # sort values of dictionary
sorted_dict = {}
for val in sorted_values:
    for k,v in student_dict.items():
# values in sorted_values are sorted so when those values approach it get appended to new sorted dict
        if val == v: 
            sorted_dict[k]=v
print("Sorted by values: ",sorted_dict)

# c) Sort dictionary using sid
print("Sorted by keys: ",sorted(student_dict.items()))

# d) Search student details using sid
student_sid = int(input("Enter the 8 digit student id whose name you want: "))
# Providing the student info only if it prexist in memory. 
if student_sid in student_dict.keys():
    print(f"{student_sid} is sid of {student_dict[student_sid]}")
else:
    print("No student with this sid")

print("****************************************QUESTION 7*************************************")    

number = int(input("Enter the number of fibbonacci sequence: "))
def fibbonaci(number):
    if number<0:
        print("Incorrect")
    elif number==0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibbonaci(number-1)+fibbonaci(number-2)             
sum = 0
for num in range(0,number):
    fibbnacci_numbers = fibbonaci(num)
    print(fibbnacci_numbers,end=" ")
    sum = sum + fibbnacci_numbers
print("\nAverage is ",(sum/number))

print("****************************************QUESTION 8*************************************")

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

# Elements in set1 and set2 but not both.
new_set1 = set1 ^ set2
print(new_set1)

# Elements that are only in one of the three sets
new_set2 = (set1|set2|set3) - (set1&set2 | set2&set3 | set1&set3)
print(new_set2)

# Elements exactly in two of the sets Set1,Set2,Set3
new_set3 = set1&set2 | set2&set3 | set1&set3
print(new_set3)

# Integers in range 1 to 10 that are not in Set1
new_set4 = {1,2,3,4,5,6,7,8,9,10} - set1
print(new_set4)

# Integers in range 1 to 10 that are not in Set1,Set2,Set3
new_set5 = {1,2,3,4,5,6,7,8,9,10} - (set1|set2|set3)
print(new_set5)
