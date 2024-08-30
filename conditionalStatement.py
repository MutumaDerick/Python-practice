# control flow is the order in which the computer executes statements in a script.
# The control flow of a Python program is regulated by conditional statements, loops, and function calls.

# Conditional statements are handled by IF statements in Python.
# An IF statement is a selection statement that allows us to choose a block of code to be executed based on a condition.

from calendar import weekday


bill = 100
discount1 = 100
if bill > 500:
    print("You get a discount of 10%")
    final_bill = bill - discount1
else:
    print("Bill is less than 500")
    print("Final bill is: " +str(bill))


# The IF statement evaluates the condition inside the parentheses.  

num = 20
if num >= 20:
    print("Number is greater than or equal to 20")

if weekday:
    print("Wake up early")
else:
    print("Sleep in")


 #  write a program for a college with a grading system as follows:
 # 90-100: A
 # 80-89: B
 # 70-79: C
 # 60-69: D
 # 50-59: E
 # 0-49: F

grade = 83

if grade >= 90:
    print("Grade  A")
elif grade >= 80:
    print("Grade B")
elif grade >= 70:
    print("Grade C")
elif grade >= 60:
    print("Grade D")
elif grade >= 50:
    print("Grade E")
else:
    print("Grade F")   
    


