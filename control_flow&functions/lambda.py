snack = lambda : print("Njugu")

# calling the lambda function
snack()
# Output: Njugu


# lambda function with arguments
def num_square(num):
    return num ** 2 # calculating the square of a number

# calling the function
print("Square of num is:", num_square(5))

# rewriting the above function using lambda
num_square = lambda num: num ** 2
# calling the lambda function
print("Square of num is:", num_square(5))