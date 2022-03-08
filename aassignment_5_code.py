print("**********************************************Question 1************************************")
from tkinter import *
Calculator = Tk()
Calculator.title("GST Calculator")
Calculator.geometry('400x400')
cost_var = IntVar()
price_var = IntVar()

def submit():      # Defining function to calculate Gst
    gst_rate = ((price_var.get()-cost_var.get())*100) / cost_var.get()
    selection = ("Your GST is: " + str(gst_rate))
    label.config(text=selection,font=12)
    cost_var.set("")
    price_var.set("")

lbl1 = Label(Calculator,text="Enter Original Cost",anchor=CENTER,font=('Arial',16))
en1 = Entry(Calculator,textvariable = cost_var,font=("calibre",12,'bold'))
lbl2 = Label(Calculator,text="Enter Net Price",anchor=CENTER,font=('Arial',16))
en2 = Entry(Calculator,textvariable = price_var,font=("calibre",12,'bold'))
# Submit button
submit_btn = Button(Calculator,text="Calculate GST",command = submit,font=("Helvetica",14))
lbl1.pack()
en1.pack()
lbl2.pack()
en2.pack()
submit_btn.pack()
label = Label(Calculator)
label.pack()
Calculator.mainloop()

print("**********************************************Question 2************************************")
from tkinter import *
tk_Calendar = Tk()
tk_Calendar.title("Calender")
tk_Calendar.geometry('400x400')

year = IntVar()

def submit():                 # Function to give calender of entered year
    import calendar
    year_calender = Tk()
    year_calender.geometry("800x800")
    year_calender.title(str(year.get())+" Calender")
    cal_ender = calendar.calendar(year.get())
    lbl = Label(year_calender,text = year.get(),font=12)
    lbl2 = Label(year_calender,text = cal_ender,font=8)
    lbl.pack()
    lbl2.pack()
    year.set("")
    year_calender.mainloop()

lbl1 = Label(tk_Calendar,text = "Enter the year",anchor=CENTER,font=('Arial',16))
en1 = Entry(tk_Calendar,textvariable=year,font=("calibre",12,'bold'))
submit_btn = Button(tk_Calendar,text="Submit",command = submit,font=("Helvetica",14))
lbl1.pack()
en1.pack()
submit_btn.pack()
tk_Calendar.mainloop()

print("**********************************************Question 3************************************")
from tkinter import *
Calculator = Tk()
Calculator.geometry('400x400')
Calculator.title("Simple Calculator")

num1var = IntVar()
num2var = IntVar()

def operation1():        # Addition operation
    operation_done = num1var.get() + num2var.get()        
    label.config(text=operation_done,font=12)
    num1var.set("")
    num2var.set("")

def operation2():         # Substraction operation
    operation_done = num1var.get() - num2var.get()
    label.config(text=operation_done,font=12)
    num1var.set("")
    num2var.set("")

def operation3():         # Multiplication operation
    operation_done = num1var.get() * num2var.get()
    label.config(text=operation_done,font=12)
    num1var.set("")
    num2var.set("")

def operation4():          # Division operation         
    operation_done = num1var.get() / num2var.get()
    label.config(text=operation_done,font=12)
    num1var.set("")
    num2var.set("")

lbl1 = Label(Calculator,text="Enter first number",anchor=CENTER,font=('Arial',16))    
lbl2 = Label(Calculator,text="Enter second number",anchor=CENTER,font=('Arial',16))  
en1 = Entry(Calculator,textvariable=num1var,font=("calibre",12,'bold'))
en2 = Entry(Calculator,textvariable=num2var,font=("calibre",12,'bold'))
btn1 = Button(Calculator,text="+",command = operation1,font=4,pady=10,padx=10)
btn2 = Button(Calculator,text="-",command = operation2,font=4,pady=10,padx=10)
btn3 = Button(Calculator,text="*",command = operation3,font=4,pady=10,padx=10)
btn4 = Button(Calculator,text="/",command = operation4,font=4,pady=10,padx=10)
label = Label(Calculator)
lbl1.pack()
en1.pack()
lbl2.pack()
en2.pack()
btn1.place(x=160,y=140)
btn2.place(x=220,y=140)
btn3.place(x=220,y=200)
btn4.place(x=160, y=200)
label.pack()
Calculator.mainloop()

print("**********************************************Question 4************************************")
e = input("Enter the list with braces[]: ")
enter = e[1:len(e)-1]
enter = enter.split(",")
enterd_list = list(map(lambda x:int(x),enter))

def divide(arr, min, max):
  pivot = arr[max]
  i = min - 1
  for j in range(min, max):
    if arr[j] <= pivot:
      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[max]) = (arr[max], arr[i + 1])
  return i + 1
def quickSort(array, low, high):
  if low < high:
    pi = divide(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

quickSort(enterd_list, 0, len(enterd_list)-1)
print('Sorted Array: ',enterd_list)

print("**********************************************Question 5************************************")
e = input("Enter the list with braces[]: ")
enter = e[1:len(e)-1]
enter = enter.split(",")
enterd_list = list(map(lambda x:int(x),enter))

enterd_list.sort()                             # Inbuilt function to sort a list
print("sorted list: ",enterd_list)

def binarySearch(arr, x, low, high):
    if low > high:                             # low>high means did not get the number we searched
        return False 
    else:
        mid = (low + high) / 2 
        mid = int(mid+1)
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return binarySearch(arr, x, mid + 1, high)
        else:        
            return binarySearch(arr, x, low, mid - 1)

search_num = int(input("Enter the number you want to search: "))  # Number to search
print(binarySearch(enterd_list,search_num,0,len(enterd_list)))

occ = int(input("Enter the number whose occurences you want: "))
print("Number of occurences is: ",enterd_list.count(occ))         # Number of occurences