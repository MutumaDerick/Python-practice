def add_nums(a, b):
    # Enclosed variable declared within the function
    answer = a + b
    def double_it():
        # Local variable declared within the nested function
        double = answer * 2
        print(double)
    double_it()
    return answer
# calling our function inside a print statement
print(add_nums(2, 3))