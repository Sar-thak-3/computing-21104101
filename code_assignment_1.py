# Question 1(**************************************************************************)
print('*************************Question 1*******************************************')

# Input of 3 numbers from user
num1 = float(input('Enter the 1st number: '))
num2 = float(input('Enter the 2nd number: '))
num3 = float(input('Enter the 3rd number: '))  

# Result shows average of 3 numbers.
result = (num1+num2+num3)/3
print(result)

# Question 2(**************************************************************************)
print('*************************Question 2*******************************************')

# Calculating tax to be paid by person.

# All amount is in dollars ($).
income = int(input('Enter your income to the nearest penny: ')) 
dependent = int(input('Enter the number of depentends: '))

# Taxable income is remaining amount after 10000 standard deduction and 3000 per dependent
tax_income = income - 10000 - (3000*dependent)

if tax_income>0:
    tax = tax_income*20/100
    print('Tax to be paid is :',tax)
else:
    print('No tax to pay')

# Question 3(**************************************************************************)
print('*************************Question 3*******************************************')
    
student1_info = [21104101,'Sarthak Garg','M','EE',9.5]
student2_info = [21104201,'Anushka','F','EE',8.0]
student3_info = [21104150,'Aditya Mengwal','M','EE',7.5]

# Displaying student info in list form.
print(student1_info)
print(student2_info)
print(student3_info)

# Question 4(**************************************************************************)
print('*************************Question 4*******************************************')

# Floating Input from user. 
marks_1 = float(input('Enter 1st marks: '))
marks_2 = float(input('Enter 2nd marks: '))
marks_3 = float(input('Enter 3rd marks: '))
marks_4 = float(input('Enter 4th marks: '))
marks_5 = float(input('Enter 5th marks: '))

# Assigning marks into list and sorting them in increasing order.
listt = [marks_1,marks_2,marks_3,marks_4,marks_5]
print(sorted(listt))

# Question 5(**************************************************************************)
print('*************************Question 5*******************************************')

colours = ['Red','Green','White','Black','Pink','Yellow']

# Part a) Remove black string in list and display remaining list 
colours.pop(3)
print('After deleting 4th colour,list is :',colours)

# Part b) Replacing 'pink' color by 'purple'.
colours[3] = 'Purple'
print(colours)