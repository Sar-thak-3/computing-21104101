print("**********************************QUESTIION 1*****************************")
def hanoitower(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    hanoitower(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    hanoitower(n-1, auxiliary, destination, source)
         
n = 3
hanoitower(n,'A','B','C')

print("**********************************QUESTIION 2*****************************")
n = int(input("Enter the number of rows you want: "))
a = n
# Factorial function
def fac(num):
    if num==0 or num==1:
        return 1
    else:
        return num * fac(num-1)

for row in range(0,n):
    for space in range(0,a-row+1):
        print(end=" ")
    for column in range(0,row+1):
        print((fac(row) // ( (fac(row-column)) * (fac(column)) )) ,end=" ")
    print()    

print("**********************************QUESTIION 3*****************************")    
num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))
if num1==0 and num2==0:
    print("Both values zeros")
elif num2==0:
    print("Function/values is not callable") 
else:
    quotient = num1//num2
    remainder = num1%num2
    print("Quotient:",quotient,"Remainder:",remainder)
    set1 = {n+quotient for (n) in range(4,7) if (n+quotient)>4}
    # Using functions created 1 liner code
    set2 = {n+remainder for n in range(4,7) if (n+remainder)>4}
    main_set = set1 | set2
    print(main_set)
    immutable_set = frozenset(main_set)
    print(immutable_set)
    max_value = max(immutable_set)
    print("Max value from set:",max_value)
    print("Hash value:",hash(max_value))

print("**********************************QUESTIION 4*****************************")    
class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no   
    def __del__(self):
        print("Object destroyed")

roll_no = int(input("Enter roll_no: "))
name = input("Enter name: ")
std1 = Student(name,roll_no)
print(std1.__dict__)
del std1

print("**********************************QUESTIION 5*****************************")
class Employees:
    def __init__(self,employee_no,salary,name):
        self.employee_no = employee_no
        self.name = name
        self.salary = salary
    def update_salary(self,new_salary):
        self.salary = new_salary

mehak = Employees(1,"Mehak",40000)
ashok = Employees(2,"Ashok",50000)
viren = Employees(3,"Viren",60000)
mehak.update_salary(70000)
print("Mehak updated salary: ",mehak.salary)
try:
    del viren
    print(viren.salary)
except:
  print("An error occurred while printing viren salary after deleting viren record")

print("**********************************QUESTIION 6*****************************")
george = input("George utter a word: ")
# Inbuilt library to call all permutations of a word
from itertools import permutations
# Making list of all permutations of word
words = [''.join(p) for p in permutations(george)]
print("Barbie can utter words: ",words)