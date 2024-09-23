# Creating a function that adds two numbers together
def add_nums():
    print(2+13)

# calling the function
def add_nums():
    print(2+13)
add_nums()

# function arguements/parameters
def add_nums(num1, num2):
    answer = num1 + num2
    print(num1 + num2)

# assign function call to a variable
total = add_nums(2, 13)  
print("Total:", total)  

# above example when the number of arguements is unknown
def add_nums(*args):
    total = 0
    for num in args:
        total += num
    return total
print("Total: ", add_nums(2, 13, 4, 5, 6, 7, 8, 9, 10))

# If the number of kwargs is unkwown, add a ** before the parameter name
def add_ages(**ages):
    sum = 0
    for k,v in ages.items():
        sum += v
    return sum
print("Total: ", add_ages(John=20, Jane=25, Doe=30, Harry=35))