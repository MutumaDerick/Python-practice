global_var = 13

def add_nums(a, b):
    # enclosed scope variable decalred within the function
    total = a + b
    print("Global_var in outer function: ", global_var)
    def double_it():
        # local variable declared within the nested function
        double = total * 2
        print("Global_var in inner function: ", global_var)
        print(double)
    double_it()
    return total

add_nums(2, 3)